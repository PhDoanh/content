---
stage: "Idea"
title: "concise SEO title (50‑60 chars)"
description: "meta description (140‑160 chars)"
permalink: ""
lang: vi
draft: true
tags: 
  - array-of-up-to-5-keywords
aliases:
  - 
cssclasses:
  - img
  - btn
socialDescription: "OG description (~100 chars)"
socialImage: "fully qualified URL to preview image"
---

# Kiểm thử đơn vị
```js
const chai = require('chai');
const assert = chai.assert;

suite('Unit Tests', function () {
  suite('Basic Assertions', function () {
    // #1
    test('#isNull, #isNotNull', function () {
      assert.isNull(null, 'This is an optional error description - e.g. null is null');
      assert.isNotNull(1, '1 is not null');
    });
    // #2
    test('#isDefined, #isUndefined', function () {
      assert.isUndefined(null, 'null is not undefined');
      assert.isUndefined(undefined, 'undefined IS undefined');
      assert.isDefined('hello', 'A string is not undefined');
    });
    // #3
    test('#isOk, #isNotOk', function () {
      assert.isNotOk(null, 'null is falsey');
      assert.isOk("I'm truthy", 'A string is truthy');
      assert.isOk(true, 'true is truthy');
    });
    // #4
    test('#isTrue, #isNotTrue', function () {
      assert.isTrue(true, 'true is true');
      assert.isTrue(!!'double negation', 'Double negation of a truthy value is true');
      assert.isNotTrue({ value: 'truthy' }, 'Objects are truthy, but are not boolean values');
    });
  });

  // -----------------------------------------------------------------------------

  suite('Equality', function () {
    // #5
    test('#equal, #notEqual', function () {
      assert.equal(12, '12', 'Numbers are coerced into strings with ==');
      assert.notEqual({ value: 1 }, { value: 1 }, '== compares object references');
      assert.equal(6 * '2', '12');
      assert.notEqual(6 + '2', '12');
    });
    // #6
    test('#strictEqual, #notStrictEqual', function () {
      assert.notStrictEqual(6, '6');
      assert.strictEqual(6, 3 * 2);
      assert.strictEqual(6 * '2', 12);
      assert.notStrictEqual([1, 'a', {}], [1, 'a', {}]);
    });
    // #7
    test('#deepEqual, #notDeepEqual', function () {
      assert.deepEqual({ a: '1', b: 5 }, { b: 5, a: '1' }, "The order of keys doesn't matter");
      assert.notDeepEqual({ a: [5, 6] }, { a: [6, 5] }, 'The order of array elements does matter');
    });
  });

  // -----------------------------------------------------------------------------

  function weirdNumbers(delta) {
    return 1 + delta - Math.random();
  }

  suite('Comparisons', function () {
    // #8
    test('#isAbove, #isAtMost', function () {
      assert.isAtMost('hello'.length, 5);
      assert.isAbove(1, 0);
      assert.isAbove(Math.PI, 3);
      assert.isAtMost(1 - Math.random(), 1);
    });
    // #9
    test('#isBelow, #isAtLeast', function () {
      assert.isAtLeast('world'.length, 5);
      assert.isAtLeast(2 * Math.random(), 0);
      assert.isBelow(5 % 2, 2);
      assert.isBelow(2 / 3, 1);
    });
    // #10
    test('#approximately', function () {
      assert.approximately(weirdNumbers(0.5), 1, 0);
      assert.approximately(weirdNumbers(0.2), 1, 0);
    });
  });

  // -----------------------------------------------------------------------------

  const winterMonths = ['dec,', 'jan', 'feb', 'mar'];
  const backendLanguages = ['php', 'python', 'javascript', 'ruby', 'asp'];
  suite('Arrays', function () {
    // #11
    test('#isArray, #isNotArray', function () {
      assert.isArray('isThisAnArray?'.split(''), 'String.prototype.split() returns an array');
      assert.isNotArray([1, 2, 3].indexOf(2), 'indexOf returns a number');
    });
    // #12
    test('Array #include, #notInclude', function () {
      assert.notInclude(winterMonths, 'jul', "It's summer in july...");
      assert.include(backendLanguages, 'javascript', 'JS is a backend language');
    });
  });

  // -----------------------------------------------------------------------------

  const formatPeople = function (name, age) {
    return '# name: ' + name + ', age: ' + age + '\n';
  };
  suite('Strings', function () {
    // #13
    test('#isString, #isNotString', function () {
      assert.isNotString(Math.sin(Math.PI / 4), 'A float is not a string');
      assert.isString(process.env.PATH, 'An env variable is a string (or undefined)');
      assert.isString(JSON.stringify({ type: 'object' }), 'JSON is a string');
    });
    // #14
    test('String #include, #notInclude', function () {
      assert.include('Arrow', 'row', "'Arrow' contains 'row'");
      assert.notInclude('dart', 'queue', "But 'dart' doesn't contain 'queue'");
    });
    // #15
    test('#match, #notMatch', function () {
      const regex = /^#\sname\:\s[\w\s]+,\sage\:\s\d+\s?$/;
      assert.match(formatPeople('John Doe', 35), regex);
      assert.notMatch(formatPeople('Paul Smith III', 'twenty-four'), regex);
    });
  });

  // -----------------------------------------------------------------------------

  const Car = function () {
    this.model = 'sedan';
    this.engines = 1;
    this.wheels = 4;
  };

  const Plane = function () {
    this.model = '737';
    this.engines = ['left', 'right'];
    this.wheels = 6;
    this.wings = 2;
  };

  const myCar = new Car();
  const airlinePlane = new Plane();

  suite('Objects', function () {
    // #16
    test('#property, #notProperty', function () {
      assert.notProperty(myCar, 'wings', "Cars don't have wings");
      assert.property(airlinePlane, 'engines', 'Planes have engines');
      assert.property(myCar, 'wheels', 'Cars have wheels');
    });
    // #17
    test('#typeOf, #notTypeOf', function () {
      assert.typeOf(myCar, 'object');
      assert.typeOf(myCar.model, 'string');
      assert.notTypeOf(airlinePlane.wings, 'string');
      assert.typeOf(airlinePlane.engines, 'array');
      assert.typeOf(myCar.wheels, 'number');
    });
    // #18
    test('#instanceOf, #notInstanceOf', function () {
      assert.notInstanceOf(myCar, Plane);
      assert.instanceOf(airlinePlane, Plane);
      assert.instanceOf(airlinePlane, Object);
      assert.notInstanceOf(myCar.wheels, String);
    });
  });

  // -----------------------------------------------------------------------------
});
```

# Kiểm thử chức năng

```js
suite('Functional Tests', function () {
  this.timeout(5000);
  suite('Integration tests with chai-http', function () {
    // #1
    test('Test GET /hello with no name', function (done) {
      chai
        .request(server)
        .keepOpen()
        .get('/hello')
        .end(function (err, res) {
          assert.equal(res.status, 200);
          assert.equal(res.text, 'hello Guest');
          done();
        });
    });
    // #2
    test('Test GET /hello with your name', function (done) {
      chai
        .request(server)
        .keepOpen()
        .get('/hello?name=xy_z')
        .end(function (err, res) {
          assert.equal(res.status, 200);
          assert.equal(res.text, 'hello xy_z');
          done();
        });
    });
    // #3
    test('Send {surname: "Colombo"}', function (done) {
      chai
        .request(server)
        .keepOpen()
        .put('/travellers')
        .send({surname: "Colombo"})
        .end(function (err, res) {
          assert.equal(res.status, 200);
          assert.equal(res.type, 'application/json');
          assert.equal(res.body.name, 'Cristoforo');
          assert.equal(res.body.surname, 'Colombo');
          done();
        });
    });
    // #4
    test('Send {surname: "da Verrazzano"}', function (done) {
      chai
        .request(server)
        .keepOpen()
        .put('/travellers')
        .send({surname: "da Verrazzano"})
        .end(function (err, res) {
          assert.equal(res.status, 200);
          assert.equal(res.type, 'application/json');
          assert.equal(res.body.name, 'Giovanni');
          assert.equal(res.body.surname, 'da Verrazzano');
          done();
        })
    });
  });
});
```

## Các cách viết kiểm thử
### Dùng callback (cách cũ, ít dùng hơn)

Ví dụ với Jest:
```js
test('callback async test', (done) => {
  function fetchData(cb) {
    setTimeout(() => cb('hello'), 100);
  }

  fetchData((data) => {
    expect(data).toBe('hello');
    done(); // phải gọi done() để báo Jest biết test đã xong
  });
});
```

⚠️ Nếu quên `done()`, test có thể bị treo hoặc fail sai.

### Dùng Promise

Jest/Mocha hiểu Promise nên chỉ cần return:

```js
test('promise async test', () => {
  function fetchData() {
    return Promise.resolve('hello');
  }

  return fetchData().then(data => {
    expect(data).toBe('hello');
  });
});
```

### Dùng async/await (thông dụng nhất)

Rõ ràng và dễ đọc:
```js
test('async/await async test', async () => {
  async function fetchData() {
    return 'hello';
  }

  const data = await fetchData();
  expect(data).toBe('hello');
});
```


## Dòng gây bất đồng bộ

```js
suite('GET /hello?name=[name] => "hello [name]"', function () {
  test('?name=John', function (done) {
    chai
      .request(server)
      .keepOpen()
      .get('/hello?name=John')
      .end(function (err, res) {
        assert.equal(res.status, 200, 'Response status should be 200');
        assert.equal(res.text, 'hello John', 'Response should be "hello John"');
        done();
      });
  });
});
```

- Có tham số `done` trong `test(...)` ⇒ nghĩa là **Mocha sẽ chờ đến khi `done()` được gọi mới kết thúc test**. Đây là cách viết test bất đồng bộ bằng **callback**.
- Nếu quên gọi `done()` ⇒ test sẽ bị timeout (fail).

Dòng gây bất đồng bộ chính là:

```js
.end(function (err, res) {
  ...
  done();
});
```

- Lý do: `chai.request(...).get(...).end(...)` sẽ **khởi tạo một HTTP request**.
- HTTP request này không trả về kết quả ngay (phải đi qua network stack, server xử lý, gửi lại response).
- Do đó, `.end(callback)` chính là nơi bạn đăng ký **callback function** để khi response từ server về, callback này mới được đẩy vào **event queue** và chạy.

## Nguyên lý dịch và chạy trong JavaScript

Đây là chỗ nhiều bạn hay nhầm, mình giải thích flow runtime:
1. **JS là ngôn ngữ đơn luồng** → chỉ có một _call stack_.
2. Khi bạn gọi:
    `chai.request(server).get('/hello?name=John').end(cb)`
    - `chai-http` sẽ gửi request qua **Node.js libuv + OS networking**.
    - Thao tác này được đưa sang **thread pool / network I/O của Node**, nên **không block** call stack chính.
3. Trong lúc chờ server phản hồi:
    - JS tiếp tục chạy các câu lệnh khác trong test (nếu có).
    - `test()` function kết thúc, nhưng Mocha chưa kết thúc test vì bạn khai báo `done`.
4. Khi server gửi response:
    - **libuv** đẩy sự kiện `"data received"` vào **event loop queue**.
    - Event loop phát hiện callback `.end(function(err, res){...})` và đưa vào call stack để thực thi.
5. Trong callback bạn gọi `done()`.
    - Mocha nhận được `done()` ⇒ đánh dấu test đã hoàn thành.

# Mô phỏng thao tác bằng Headless Browser

👉 **Headless browser** là **trình duyệt web không có giao diện đồ họa** – nó vẫn render HTML, CSS, chạy JavaScript… như một trình duyệt thật (Chrome, Firefox), nhưng không hiện cửa sổ UI.

📌 Đặc điểm
- Chạy ở chế độ nền (background), không hiển thị giao diện.
- Có thể điều khiển bằng code (API hoặc script).
- Hữu ích cho tự động hóa (automation).

⚡ Ứng dụng phổ biến
1. **Web scraping** → lấy dữ liệu từ web động (SPA, AJAX).
2. **Kiểm thử tự động (test automation)** → giả lập người dùng truy cập, click, nhập form.
3. **SEO / Render trước (pre-rendering)** → render trang SPA để Google bot đọc được.
4. **Screenshot / PDF** → chụp trang web, xuất báo cáo.

🔧 Công cụ phổ biến
- **Puppeteer** (Google Chrome headless).
- **Playwright** (MS).
- **Selenium + headless Chrome/Firefox**.
- **PhantomJS** (giờ ít dùng, đã deprecated).

=> **Zombie.js** là một **headless browser cho Node.js**.


## AJAX Request 
👉 **AJAX request** là một cách để **gửi yêu cầu HTTP bất đồng bộ từ trình duyệt đến server** mà **không cần reload lại toàn bộ trang web**.

📌 Giải thích
- **AJAX** = **Asynchronous JavaScript and XML** (tên cũ, nhưng giờ không chỉ dùng XML mà còn JSON, HTML, text).
- Nó cho phép trang web:
    - Gửi/nhận dữ liệu với server "ngầm" phía sau.
    - Chỉ cập nhật một phần giao diện (DOM) thay vì tải lại cả trang.

⚡ Ví dụ trực quan: Khi bạn nhập từ khóa vào ô tìm kiếm Google và kết quả gợi ý hiện ra tức thì → đó là AJAX request.

```js
const Browser = require('zombie');
Browser.site = 'https://3000-freecodecam-boilerplate-k0byx7gahru.ws-us121.gitpod.io'

suite('Functional Tests with Zombie.js', function () {
  this.timeout(5000);
  const browser = new Browser();

  suiteSetup(function(done) {
    return browser.visit('/', done);
  });

  suite('Headless browser', function () {
    test('should have a working "site" property', function() {
      assert.isNotNull(browser.site);
    });
  });

  suite('"Famous Italian Explorers" form', function () {
    // #5
    test('Submit the surname "Colombo" in the HTML form', function (done) {
      browser.fill('surname', 'Colombo').then(() => {
        browser.pressButton('submit', ()=>{
          browser.assert.success();
          browser.assert.text('span#name', 'Cristoforo');
          browser.assert.text('span#surname', 'Colombo');
          browser.assert.elements('span#dates', 1);
          done();
        })
      })
    });
    // #6
    test('Submit the surname "Vespucci" in the HTML form', function (done) {
      browser.fill('surname', 'Vespucci').then(()=>{
        browser.pressButton('submit', ()=>{
          browser.assert.success();
          browser.assert.text('span#name', 'Amerigo');
          browser.assert.text('span#surname', 'Vespucci');
          browser.assert.elements('span#dates', 1);
          done();
        })
      })

    });
  });
});
```
