---
title: "Rails Model Foundations: Migrations, Validations và bcrypt"
description: "Khám phá Rails Model Foundations qua migrations, validations, has_secure_password với bcrypt và model tests - nền tảng ActiveRecord bền vững từ Hartl Chapter 6."
permalink: "/system-foundations/rails-model-foundations/"
lang: vi
publish: false
updated: 2026-09-01
tags:
  - GenAI
  - Intermediate
  - fullstack
  - system-foundations
aliases:
  - rails-model-foundations
cssclasses:
  - img
socialDescription: "Rails migrations, validations và has_secure_password - nền tảng Model bền vững từ Hartl Ch.6"
socialImage: "/images/rails-model-foundations-1200x630.png"
---

<!-- OG image asset placeholder: /images/rails-model-foundations-1200x630.png - 1200x630 PNG required for og:image; create asset before publish (Quartz static/images) -->

Tôi từng nghĩ tạo bảng users chỉ là `CREATE TABLE` rồi xong, cho tới khi một lần đổi tên cột trên staging làm sập deploy vì thiếu migration rollback. Tôi chạy `rails db:migrate:status` và thấy một migration ở trạng thái down, schema trên server lệch với code. Trải nghiệm đó cho thấy Model trong Rails không chỉ là class Ruby - nó là hợp đồng giữa code, schema versioned và dữ liệu sản xuất. Bài này đi theo đúng thứ tự Hartl Chapter 6 để khóa từng tầng một cách có kỷ luật.

> [!tldr] Tóm tắt
> - Migrations là file Ruby versioned tiến hóa schema; `db/schema.rb` là snapshot authoritative
> - Validations chạy trước `save` với `presence/length/format/uniqueness`; `uniqueness` cần index duy nhất ở DB để tránh race condition
> - `has_secure_password` dùng bcrypt lưu `password_digest`, cung cấp `authenticate` constant-time
> - Model tests kế thừa `ActiveSupport::TestCase`, dùng `setup` + `valid?`/`invalid?` để khóa chặt mọi validation
> - Quy trình Chapter 6: migrations -> validations -> secure password -> tests tạo vòng khép kín evergreen

## Vì sao Rails Model Foundations quyết định độ bền ứng dụng?

Hãy tưởng tượng Model như bản thiết kế nhà. Migrations là móng, đổ một lần và ghi lại từng lần sửa. Validations là quy chuẩn xây dựng, chặn vật liệu sai trước khi dựng tường. `has_secure_password` là khóa cửa, không phải ổ khóa giả. Tests là kiểm định, gõ búa vào từng mối nối để chắc không sập khi có người ở. Thiếu một trụ, nhà vẫn đứng tạm, nhưng gió lớn sẽ lộ.

**Trả lời nhanh:** Model là lớp duy nhất chạm cả ba tầng - Ruby, SQL và dữ liệu người dùng - nên lỗi ở Model lan ra toàn hệ thống; Hartl Chapter 6 chọn đúng thứ tự migrations -> validations -> `has_secure_password` -> tests để khóa từng tầng.

Tôi thấy nhiều team bắt đầu từ controller rồi vá model sau. Controller chết sau mỗi request, model sống cùng dữ liệu nhiều tháng. Một validation thiếu hôm nay thành dữ liệu bẩn ngày mai.

Bốn trụ trong [[Chapter 6. Modeling Users]] tạo chuỗi phụ thuộc: không có cột `password_digest` thì `has_secure_password` vô nghĩa. Không có validation thì test không có gì để assert.

Case [[F2T LOOP Corrections and Quality Evaluation (Analysis)]] cho thấy giá khi thiếu ràng buộc ở model. QualityEvaluator chỉ đếm ticket đã review (`approved`/`committed`) trên rolling window 20. Nếu đếm cả `pending_review`, accuracy bị thổi phồng và project thăng cấp sớm.

> [!tip] Đọc thêm
> Nếu bạn mới với Rails, hãy đọc [[Ruby on Rails MVC]] trước để đặt Model đúng chỗ trong tam giác M-V-C, rồi quay lại đây với bản đồ 4 trụ trong đầu.

<!-- Image placement: diagram 4 trụ Model Foundations, alt="Sơ đồ 4 trụ Rails Model Foundations theo Hartl Chapter 6" -->

## Migrations: schema versioned, reversible và authoritative ở schema.rb

Nghĩ về migrations như git log cho database. Mỗi file là một commit: tạo bảng, thêm cột, thêm index. Rails chạy chúng theo timestamp, và `db/schema.rb` là bản build cuối cùng.

**Trả lời nhanh:** Migrations là file Ruby có timestamp trong `db/migrate`, mô tả thay đổi schema theo thời gian; `rails db:migrate` áp tuần tự và `db/schema.rb` luôn là snapshot chuẩn để `db:schema:load`.

Tôi chạy lệnh quen thuộc:

```sh
rails generate model User name:string email:string
```

Rails sinh ra bốn thứ cùng lúc: `db/migrate/YYYYMMDDHHMMSS_create_users.rb`, `app/models/user.rb`, `test/models/user_test.rb` và `test/fixtures/users.yml`. File migration trông như thế này ([Rails Guides - Active Record Migrations](https://guides.rubyonrails.org/active_record_migrations.html), retrieved 2026-09-01):

```ruby
class CreateUsers < ActiveRecord::Migration[7.0]
  def change
    create_table :users do |t|
      t.string :name
      t.string :email
      t.timestamps
    end
  end
end
```

`create_table` tự tạo cột `id` kiểu bigint. `t.timestamps` thêm `created_at` và `updated_at`. Method `change` tự reversible với `create_table`, `add_column`, `add_index`; thao tác phức tạp thì tách `up`/`down`.

Thêm cột sau này tuân quy ước tên:

```sh
rails generate migration add_password_digest_to_users password_digest:string
```

Rails suy luận `add_column` từ tên migration như ví dụ ở trên.

`db/schema.rb` được sinh tự động sau mỗi migrate, luôn commit vào git. Trên CI, `rails db:schema:load` nhanh hơn chạy lại hàng trăm migration. [[ActiveRecord Migrations]] ghi rõ: schema là snapshot, migrations là lịch sử.

> [!warning] Lưu ý phiên bản
> `ActiveRecord::Migration[7.0]` khóa API theo phiên bản Rails. Khi bạn nâng Rails, giữ nguyên số này trong file cũ, chỉ file mới dùng số mới. Đổi bừa sẽ làm rollback sai.

<iframe width="560" height="315" src="https://www.youtube.com/embed/FBu6y2E0D9o" title="Rails Migrations Explained - GoRails" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy"></iframe>

<!-- Image placement: screenshot migration file, alt="File migration CreateUsers với change và timestamps" -->

## Validations: bốn khiên presence, length, format, uniqueness

Nếu migrations là móng, validations là người gác cửa. Mỗi bản ghi phải qua bốn khiên trước khi chạm DB: có mặt, độ dài hợp lệ, định dạng đúng, và không trùng.

**Trả lời nhanh:** `validates` là chốt chặn trước `create/save/update`; nếu fail thì trả `false` và điền `errors`, giúp UI báo lỗi mà không chạm DB.

Tôi định nghĩa model như Hartl gợi ý:

```ruby
class User < ApplicationRecord
  validates :name,  presence: true, length: { maximum: 50 }
  validates :email, presence: true, length: { maximum: 255 },
                    format: { with: VALID_EMAIL_REGEX },
                    uniqueness: { case_sensitive: false }
  validates :password, presence: true, length: { minimum: 6 }
end
```

`presence: true` chặn `nil`, `""` và `"   "` - quan trọng vì form thường gửi chuỗi rỗng ([Rails Guides - Active Record Validations](https://guides.rubyonrails.org/active_record_validations.html), retrieved 2026-09-01).

`length` hỗ trợ `minimum`, `maximum`, `in: 6..20`, `is: 10`. `format` dùng regex với neo `\A` và `\z` để khớp toàn chuỗi:

```ruby
VALID_EMAIL_REGEX = /\A[\w+\-.]+@[a-z\d\-.]+\.[a-z]+\z/i
```

Thiếu `\A`/`\z`, chuỗi như `user@example,com` có thể lọt như đã dẫn ở phần validations trên. `uniqueness: true` là khiên mềm ở tầng Ruby, sẽ khóa cứng ở H2 sau.

Kiểm tra nhanh:

```ruby
user.valid?              # true nếu không lỗi
user.errors.full_messages # ["Email has already been taken"]
```

| Method | Khi fail |
|--------|----------|
| `save` / `update` | Trả `false` |
| `save!` / `update!` | Raise `RecordInvalid` |
| `update_attribute` | Ghi thẳng, bỏ qua validations |

Tôi tránh `update_attribute` vì nó bỏ qua mọi khiên. [[ActiveRecord Validations]] và [[Rails Model Tests]] nhấn mạnh cạm bẫy này.

> [!note] Mẹo nhỏ
> Khi debug, gọi `user.valid?` rồi `user.errors.full_messages` ngay trong console thay vì đoán. Thông điệp lỗi là nguồn chân lý nhanh nhất.

## Ràng buộc DB và index: khi validation ở app là chưa đủ

Tôi từng tin validation ở model là đủ, cho tới khi hai request đăng ký cùng email chạy song song và cả hai đều `valid?`. Hai `INSERT` cùng qua, DB không phàn nàn, và tôi có duplicate. Vấn đề là timing.

**Trả lời nhanh:** Validation ở model chạy ở tầng Ruby nên hai request song song có thể cùng vượt qua; chỉ `add_index ... unique: true` ở DB mới đảm bảo duy nhất tuyệt đối.

Hai request cùng kiểm `exists?` -> false, cùng `INSERT` -> duplicate nếu thiếu index. Đây là race condition kinh điển.

Giải pháp là defense in depth: validation cho UX, DB constraint cho toàn vẹn dữ liệu:

```ruby
add_index :users, :email, unique: true
```

Dòng này tạo B-Tree unique ở DB, chặn duplicate dù app có race. Tôi thêm `null: false` ngay từ đầu cho cột quan trọng để tránh NULL lọt qua unique index.

Case [[F2T LOOP Corrections and Quality Evaluation (Analysis)]] cho ví dụ về ghi đè: F2T dùng `lock_version` để tránh last-write-wins. Lệch version -> `StaleObjectError` -> 422 để client refresh.

| Tầng | Chặn gì | Ví dụ |
|------|---------|-------|
| Model validation | Lỗi nhập liệu thường | `validates :email, presence: true` |
| DB constraint | Race condition | `add_index :users, :email, unique: true` |
| Optimistic locking | Ghi đè đồng thời | `lock_version` |

Mọi `uniqueness: true` phải đi kèm `add_index ... unique: true`. [[Optimistic Locking]] là bước tiếp khi có ghi đồng thời thực sự.

> [!warning] Sai lầm phổ biến
> Thêm `uniqueness: true` mà quên index sẽ qua hết test đơn luồng, nhưng sập ở tải song song. Hãy chạy test concurrency hoặc ít nhất kiểm `db/schema.rb` có `unique: true` trước khi merge.

<!-- Image placement: diagram race condition, alt="Hai request cùng validate rồi cùng insert gây duplicate" -->

## has_secure_password và bcrypt: không bao giờ lưu plaintext

Mật khẩu là thứ duy nhất bạn không bao giờ được nhìn thấy lại sau khi người dùng gõ. Tôi từng thấy codebase lưu plaintext để "debug dễ". Đó là cửa mở cho rò rỉ.

**Trả lời nhanh:** `has_secure_password` (cần gem `bcrypt` + cột `password_digest`) tự băm mật khẩu bằng Blowfish salted cost 2^12, lưu hash và cung cấp `authenticate(plaintext)` so sánh constant-time.

Setup chỉ ba bước, nhưng thiếu một bước là lỗi ngay:

```ruby
# Gemfile
gem "bcrypt", "~> 3.1.7"
```
```ruby
# Migration
class AddPasswordDigestToUsers < ActiveRecord::Migration[7.0]
  def change
    add_column :users, :password_digest, :string
  end
end
```
```ruby
# Model
class User < ApplicationRecord
  has_secure_password
  validates :password, length: { minimum: 6 }
end
```

`has_secure_password` thêm `password=` (băm vào `password_digest`), `password_confirmation=` và `authenticate(plaintext)` ([Rails API - ActiveModel::SecurePassword](https://api.rubyonrails.org/classes/ActiveModel/SecurePassword/ClassMethods.html), retrieved 2026-09-01). Hai user cùng mật khẩu vẫn cho hash khác nhau vì salt.

```ruby
user = User.create!(name: "An", email: "an@example.com", password: "foobar", password_confirmation: "foobar")
user.authenticate("foobar") # => user
user.authenticate("wrong")  # => false
```

Cost 12 nghĩa là 4096 vòng, tốn ~250 ms, đủ chậm để chống brute-force ([OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html), retrieved 2026-09-01; [bcrypt gem](https://github.com/bcrypt-ruby/bcrypt-ruby), retrieved 2026-09-01). OWASP khuyến nghị chỉnh cost sao cho băm tốn 250-500 ms.

| Cost | Vòng | Thời gian | Ghi chú |
|------|------|-----------|---------|
| 10 | 1,024 | ~60 ms | Nhanh, yếu hơn |
| 12 | 4,096 | ~250 ms | Mặc định Rails |
| 14 | 16,384 | ~1 s | Chậm, UX kém |

`authenticate` so sánh constant-time, tránh timing attack như Rails API đã mô tả ở trên. Validation tự thêm chỉ có presence khi tạo mới, bạn cần tự thêm `validates :password, length: { minimum: 6 }`.

> [!tip] Đọc thêm
> Sau khi nắm bcrypt, hãy xem [[ActiveRecord Secure Password]] để đào sâu cost và cấu trúc hash.

<iframe width="560" height="315" src="https://www.youtube.com/embed/X_qcHoqitUs" title="Has Secure Password in Rails - Bcrypt Explained" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy"></iframe>

<!-- Image placement: minh họa chuỗi bcrypt hash, alt="Cấu trúc chuỗi bcrypt với algorithm, cost và hash" -->

## Rails Model Tests: khóa validations bằng ActiveSupport::TestCase

Tôi viết test model không phải để đạt coverage, mà để khóa hành vi. Mỗi validation có một test khóa, xóa validation là test đỏ ngay.

**Trả lời nhanh:** Model tests sống ở `test/models/user_test.rb`, kế thừa `ActiveSupport::TestCase`, dùng `setup` tạo `@user` hợp lệ rồi đổi từng field để assert `valid?`/`invalid?`.

Khung chuẩn từ [[Rails Model Tests]]:

```ruby
require "test_helper"

class UserTest < ActiveSupport::TestCase
  def setup
    @user = User.new(name: "Example User", email: "user@example.com",
                     password: "foobar", password_confirmation: "foobar")
  end

  test "should be valid" do
    assert @user.valid?
  end
end
```

`setup` là Arrange. Mỗi test đổi một field thành invalid rồi `assert_not @user.valid?`.

Các pattern tôi dùng:

```ruby
test "name should be present" do
  @user.name = "   "
  assert_not @user.valid?
end

test "email validation should accept valid addresses" do
  valid_addresses = %w[user@example.com USER@foo.COM A_US-ER@foo.bar.org
                       first.last@foo.jp alice+bob@baz.cn]
  valid_addresses.each do |valid_address|
    @user.email = valid_address
    assert @user.valid?, "#{valid_address.inspect} should be valid"
  end
end

test "email addresses should be unique" do
  duplicate_user = @user.dup
  @user.save
  assert_not duplicate_user.valid?
end

test "password should be present (nonblank)" do
  @user.password = @user.password_confirmation = " " * 6
  assert_not @user.valid?
end
```

Fixtures nạp trước mỗi test khi `fixtures :all` bật:

```yaml
michael:
  name: Michael Example
  email: michael@example.com
  password_digest: <%= User.digest("password") %>
```

Model tests kế thừa `ActiveSupport::TestCase`, không cần `get`/`post` như controller tests ([Rails Guides - Testing](https://guides.rubyonrails.org/testing.html), retrieved 2026-09-01).

Lệnh chạy:

```sh
rails test                 # tất cả
rails test:models           # chỉ model
rails test test/models/user_test.rb  # một file
```

Tôi chạy `rails test:models` trước mỗi commit liên quan đến User. Nếu test xanh, tôi mới nghĩ tới controller. [[TDD Red-Green-Refactor]] và [[Rails Testing]] là hai neo để mở rộng từ model sang integration.

> [!note] Gợi ý thực hành
> Viết test presence trước, rồi length, rồi format, rồi uniqueness. Mỗi bước thêm một `validates` và chạy test tới xanh. Nhịp red-green nhỏ giúp bạn không quên nhánh nào.

<!-- Image placement: code test valid? và authenticate, alt="Đoạn test User với assert valid và authenticate" -->

## Từ migrations tới tests: quy trình khép kín và checklist production

Mỗi trụ đứng riêng đã tốt, nhưng giá trị thật nằm ở thứ tự. Migrations trước, validations sau, bcrypt sau nữa, tests khóa cuối. Đảo thứ tự, bạn sẽ vá lỗi thay vì ngăn lỗi.

**Trả lời nhanh:** Quy trình khép kín là: sinh migration -> chạy migrate -> thêm validations + `has_secure_password` -> viết test khóa lại -> thêm index DB -> review qua case F2T LOOP để thấy thiếu gì sẽ đau ở production.

Checklist trước mỗi deploy có đụng tới User:

1. `rails db:migrate:status` sạch, `db/schema.rb` đã commit, `db:schema:load` chạy được trên CI.
2. Validations đủ bốn loại, mỗi loại có test valid/invalid, biên `51` và `5` đều có.
3. `password_digest` là string, `bcrypt` đã bundle, `has_secure_password` bật.
4. `add_index :users, :email, unique: true` có trong schema.
5. `rails test:models` xanh, `authenticate` test cả đúng/sai.

Thứ tự không đảo được: thiếu cột thì `has_secure_password` lỗi ngay. Bài học từ [[F2T LOOP Corrections and Quality Evaluation (Analysis)]]: QualityEvaluator dùng `pluck(:id)` và `where(state: REVIEWED_STATES)` để tránh thổi phồng accuracy - ràng buộc phải ở DB.

| Bước | Tạo gì | Kiểm gì |
|------|--------|---------|
| 1. Migrations | `create_users`, `add_index unique` | `db:migrate:status` sạch |
| 2. Validations | `presence/length/format/uniqueness` | `valid?` |
| 3. Secure password | `bcrypt` + `has_secure_password` | `authenticate` |
| 4. Model tests | `setup` + assertions | `rails test:models` xanh |

Tôi hay hỏi: nếu xóa một dòng `validates`, test nào sẽ đỏ? Nếu không có câu trả lời, tức là thiếu test. Sau khi khóa xong User, hướng mở rộng là [[Optimistic Locking]] khi nhiều người sửa cùng bản ghi.

> [!tip] Checklist bàn giao
> Trước khi merge, mở `db/schema.rb` và đọc to: email có `unique: true` không, `password_digest` là string không, `lock_version` có nếu cần concurrency không. Nếu thiếu, thêm migration, đừng vá bằng validation.

<!-- Image placement: checklist production, alt="Checklist bàn giao Model Foundations trước khi deploy" -->

## Câu hỏi thường gặp

> [!question] Migrations khác schema.rb thế nào?
> Migrations là các file thay đổi tăng dần theo thời gian; `schema.rb` là ảnh chụp tổng hợp sau khi chạy hết migrations. Deploy production thường dùng `db:schema:load` từ schema để nhanh và ít lỗi hơn chạy lại chuỗi migrations dài.

> [!question] Vì sao uniqueness validation cần thêm unique index ở DB?
> Vì validation chỉ kiểm tra ở tầng Ruby trước khi INSERT. Hai request đồng thời có thể cùng thấy "chưa tồn tại" rồi cùng ghi, tạo trùng lặp. `add_index :users, :email, unique: true` khóa ở tầng DB, chặn race condition.

> [!question] has_secure_password có tự validate độ dài mật khẩu không?
> Không. Nó chỉ tự thêm presence khi tạo mới và kiểm tra confirmation khi có field. Bạn cần tự thêm `validates :password, length: { minimum: 6 }` và test với `password = "a"*5` để đảm bảo.

> [!question] Nên dùng save, save! hay update_attribute?
> Dùng `save`/`update` khi muốn tôn trọng validations và xử lý `false`; dùng `save!` khi muốn raise lỗi ngay (ví dụ seeds). Tránh `update_attribute` vì nó bỏ qua validations, dễ ghi dữ liệu bẩn.

## Kết luận

Rails Model Foundations không phải mẹo vặt mà là kỷ luật: migrations giữ lịch sử schema minh bạch, validations chặn dữ liệu bẩn sớm, bcrypt bảo vệ mật khẩu bằng toán học, và model tests khóa tất cả lại bằng `valid?`. Đi đúng thứ tự Hartl Chapter 6 giúp bạn tránh những lỗi production đắt giá - từ duplicate email do thiếu index tới plaintext lộ ra vì thiếu `password_digest`. Từ đây, hãy đào sâu [[Optimistic Locking]] và [[Rails Testing]] để thấy Model bền vững vận hành thế nào khi có concurrency thực sự.

<!--
## Vùng liên kết nội bộ (Internal Linking Zones)
- [[ActiveRecord Migrations]] - trụ schema versioned, bổ sung cho H2 migrations và schema.rb
- [[ActiveRecord Validations]] - chi tiết 4 validators, neo cho H2 validations
- [[ActiveRecord Secure Password]] - bcrypt và authenticate, neo cho H2 has_secure_password
- [[Rails Model Tests]] - mẫu setup/valid?/fixtures, neo cho H2 model tests
- [[Chapter 6. Modeling Users]] - hub tổng hợp Hartl, neo cho H2 mở đầu và kết luận
- [[Ruby on Rails MVC]] - bối cảnh Model trong MVC, đặt ở H2 vì sao foundations quan trọng
- [[Rails Testing]] - mở rộng từ model tests sang controller/integration tests
- [[TDD Red-Green-Refactor]] - phương pháp viết test trước khi thêm validation
-->

<!--
## Khoảng trống nội dung cần khai thác (Content Gaps to Exploit)
1. Thiếu benchmark Việt hóa về cost factor bcrypt (so PNG vs JPG của bài trước - cần số thực tế 10 vs 12 trên Rails 7)
2. Chưa có so sánh validates vs DB constraints qua ví dụ race condition tái hiện bằng script song song
3. Thiếu ảnh chụp lỗi thiếu password_digest khi gọi has_secure_password - PAA hay hỏi
4. Chưa khai thác fixtures vs factories (FactoryBot) - SERP top 5 đều đề cập, bài này bỏ ngỏ để tạo bài follow-up
5. Thiếu sơ đồ migration lifecycle (generate -> migrate -> rollback -> schema:load) - gap visual
-->

<!--
SEO & GEO
Primary: Rails ActiveRecord migrations
Secondary: ActiveRecord validations Rails, has_secure_password bcrypt, Rails model tests, Rails Modeling Users Hartl, VALID_EMAIL_REGEX, add_index unique true, password_digest authenticate
Intent: Informational + how-to - evergreen explainer cho dev tìm migrations/validations/secure password/testing
Word count plan: ~2900w (7 H2 × ~350w + FAQ 200w + intro/conclusion 250w) - trong ngưỡng 1500-3000, không cần atomize
Template: tutorial - code walkthrough + how-to-guide hybrid (phù hợp search intent Informational how-to)
Flesch target: 60-70
-->
