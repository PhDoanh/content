---
stage: Publish
title: "Ringurooma Koe API：日本語音声サービスを提供する"
description: ""
permalink: 
lang: ja
draft: false
tags:
  - rest-api
  - japanese-voice
  - azure-speech-sdk
  - text-to-speech
  - intent-recognition
  - pronunciation-assessment
  - real-time-recognition
aliases: 
cssclasses:
  - img
  - btn
socialDescription: ""
socialImage: ""
---
%% translated by machine %%

> 元の名前: リングローマの音声API

このリポジトリは、 [Ringurooma](https://github.com/HuyDang05/Ringurooma) プロジェクトによって独自に開発された、日本語のスピーキング スキルを処理および評価するために Azure Speech SDK と通信する中間マイクロサービスです。したがって、REST API をサポートするすべてのアプリケーションで使用できます。

# 特徴

- **音声テキスト変換**:日本語の音声を認識してテキストに変換します
- **発音評価**:日本語の発音精度評価(100点満点)
- **イントネーションとトーン分析**:日本語を話すときのイントネーションの自然さを評価する
- **スピーキングスピード評価**:スピーキングスピードが適切かどうかを分析および評価します
- **語彙アクセント分析**: 単語内のアクセントの正しい配置を評価する
- **長所と短所の分析**: スピーキングスキルの長所と短所を特定する
- **改善の提案**:日本語のスピーキングスキルを向上させるための提案をします

# API エンドポイント

すべての API エンドポイントでは、 `X-API-Key` ヘッダーまたはクエリ パラメーター `api_key` を介した API キーによる認証が必要です。

## GET `/`

- **説明**: サーバーの動作状態を確認する
- **応答**: バージョンとステータス情報
- **応答の例**:

```json
{
  "message": "Ringurooma Speech API Server",
  "version": "1.0.0",
  "status": "running",
  "features": [
    "Speech to Text (POST /api/speech-to-text)",
    "Real-time Speech to Text (WebSocket)",
    "Pronunciation Assessment (POST /api/pronunciation-assessment)",
    "Text to Speech (POST /api/text-to-speech)",
    "Intent Recognition (POST /api/intent-recognition)"
  ]
}
```

## POST `/api/speech-to-text`

- **説明**: オーディオをテキストに変換する
- **Content-Type**: `multipart/form-data` または `application/json` (base64 を使用している場合)
- **パラメータ**:
	- **ファイルの使用状況**:
		- `audio`: オーディオファイル(WAV) - *必須*
		- `user_id`: ユーザー ID - *オプション*
	- **base64 の使用**:
		- `audio_base64`: Base64 のオーディオ文字列 - *必須*
		- `user_id`: ユーザー ID - *オプション*
		- **ヘッダー**:
			- `X-Audio-Format`: `base64` - *必須*
- **制限**:最大ファイルサイズ10MB
- **応答**: 音声から認識されたテキスト
- **応答の例**:

```json
{
  "user_id": "test-user-001",
  "transcription": "こんにちは、私の名前は田中です。",
  "timestamp": "2025-05-18T07:31:28.123Z"
}
```

## POST `/api/pronunciation-assessment`

- **説明:** 音と参照テキストに基づく日本語の発音評価
- **Content-Type**: `multipart/form-data` または `application/json` (base64 を使用している場合)
- **パラメータ**:
	- **ファイルの使用状況**:
		- `audio`: オーディオファイル(WAV) - *必須*
		- `reference_text`: 日本語参考テキスト - *必須*
		- `user_id`: ユーザー ID - *オプション*
	- **base64 の使用**:
		- `audio_base64`: Base64 のオーディオ文字列 - *必須*
		- `reference_text`: 日本語参考テキスト - *必須*
		- `user_id`: ユーザー ID - *オプション*
		- **ヘッダー**:
			- `X-Audio-Format`: `base64` - *必須*
			- `Content-Type`: `application/json` - *必須*
- **制限**:最大ファイルサイズ10MB
- **回答**:詳細なレビュー結果
- **応答の例**:

```json
{
  "user_id": "test-user-001",
  "reference_text": "こんにちは、私の名前は田中です。",
  "transcription": {
    "fromRecognition": "こんにちは、私の名前は田中です。",
    "fromAssessment": "こんにちは、私の名前は田中です。"
  },
  "jlpt_level": "N3",
  "pronunciation_scores": {
    "accuracy": 85.7,
    "fluency": 79.3,
    "completeness": 95.0,
    "pronunciation": 82.5,
    "prosody": 75.2
  },
  "speech_rate": {
    "words_per_minute": 120,
    "assessment": {
      "rating": "good",
      "feedback": "Tốc độ nói phù hợp, gần với tốc độ nói tự nhiên của người bản xứ."
    }
  },
  "word_stress": {
    "overall_score": 76.5,
    "details": [...]
  },
  "analysis": {
    "strengths": ["Phát âm chính xác các từ vựng", "Nói đầy đủ nội dung so với văn bản tham chiếu"],
    "weaknesses": ["Ngữ điệu chưa tự nhiên, còn đơn điệu"],
    "improvement_suggestions": ["Nghe và bắt chước ngữ điệu của người bản xứ, tập trung vào cao độ và trọng âm"]
  },
  "word_details": [...],
  "phoneme_details": [...],
  "benchmark_comparison": {
    "accuracy_vs_benchmark": "5.70",
    "fluency_vs_benchmark": "-0.70",
    "overall_vs_benchmark": "2.50"
  },
  "timestamp": "2025-05-18T07:31:28.123Z"
}
```

## POST `/api/text-to-speech`

- **説明: テキスト読み上げ変換**
- **コンテンツタイプ**: `application/json`
- **パラメータ**:
	- `text`: 音声に変換する必要があるテキスト - *必須*
	- `voice_name`: 音声名 (デフォルト: 'ja-JP-NanamiNeural') – *オプション*
- **応答**: MP3 オーディオ ファイル
- **応答ヘッダー**:
	- `コンテンツタイプ`: `オーディオ/mp3`
	- `コンテンツ-性質`:添付ファイル。ファイル名="tts-\[タイムスタンプ\].mp3"

## POST /api/インテント認識

- **説明**: テキストまたは音声から意図を特定する
- **コンテンツタイプ**: `multipart/form-data` または `application/json`
- **パラメータ**:
	- **入力はテキスト** (application/json)です。
		- `text`: インテントの識別が必要なテキスト - *必須*
		- `user_id`: ユーザー ID - *オプション*
	- **入力はオーディオ(**マルチパート/フォームデータ)です。
		- `audio`: オーディオファイル(WAV) - *必須*
		- `user_id`: ユーザー ID - *オプション*
	- **入力は base64** オーディオ (application/json) です。
		- `audio_base64`: Base64 のオーディオ文字列 - *必須*
		- `user_id`: ユーザー ID - *オプション*
		- **ヘッダー**:
			- `X-Audio-Format`: `base64` - *必須*
- **制限**:最大ファイルサイズ10MB(オーディオ入力の場合)
- **応答**: インテント認識の結果
- **応答の例**:

```json
{
  "user_id": "test-user-001",
  "query": "こんにちは、初めまして。お願いします。",
  "intent": {
    "top": "Greeting",
    "confidence": 0.5
  },
  "intents": {
    "Greeting": 2,
    "Request": 1,
    "Farewell": 0,
    "Question": 0,
    "Affirmation": 0,
    "Negation": 0,
    "Opinion": 0
  },
  "entities": [],
  "timestamp": "2025-05-18T07:45:12.456Z"
}
```

## WebSocket エンドポイント - リアルタイム音声認識

- **説明**: リアルタイム音声認識のための WebSocket 接続
- **プロトコル**: WebSocket (ws:// または wss://)
- **プロセス**:
	1. WebSocket エンドポイントへの接続
	2. start コマンドを送信する: `{"command": "start"}`
	3. オーディオデータをバイナリデータとして送信する
	4. リアルタイムの認識結果を取得する
	5. 停止コマンドの送信: `{"command": "stop"}`
- **サーバーからのメッセージ形式**:

```json
{
  "type": "recognition",
  "result": {
    "type": "recognizing", // hoặc "recognized"
    "text": "こんにちは",
    "isFinal": false // true nếu là kết quả cuối cùng
  }
}
```

# JLPTレベルマッピング

このサービスは、発音スコアに基づいてJLPTレベルを自動的に決定します。

| JLPTレベル | 発音ポイント |
| ---------- | ------------ |
| N1         | 90-100       |
| N2         | 80-89        |
| N3         | 70-79        |
| N4         | 60-69        |
| N5         | <60          |

# インストールして実行する

## 必要条件

- Node.js 14+
- Azure Speech Service アカウント
- Azure Speech SDK を使用するためのインターネット接続

## 手動インストール

1. リポジトリのクローン
2. 依存関係のインストール: `npm install`
3. 環境を構成する: 次の変数を使用して `.env` ファイルを作成します。

```
SPEECH_KEY=your_azure_speech_key
SPEECH_REGION=your_azure_region
API_KEY=your_api_authentication_key
PORT=3000 (optional)
```

4. サービスを実行します: `node server.js` または `npm start`

## Docker を使用してデプロイする

1. Docker と Docker Compose がインストールされていることを確認します
2. 必要な環境変数を含む `.env` ファイルを作成します。
3. 実行:`docker-compose up -d`

## SSL/HTTPS 設定

`setup-ssl.sh` スクリプトを使用して、Let's EncryptでSSLを設定します。

```bash
./setup-ssl.sh your-domain.com
```

# cURL での API の使用例

## 音声をテキストに変換する (ファイルを使用)

```bash
curl -X POST \
  -H "X-API-Key: your_api_key" \
  -F "audio=@/path/to/audio.wav" \
  -F "user_id=test-user" \
  https://your-domain.com/api/speech-to-text
```

## 発音の評価(ファイルを使用)

```bash
curl -X POST \
  -H "X-API-Key: your_api_key" \
  -F "audio=@/path/to/audio.wav" \
  -F "reference_text=こんにちは、私の名前は田中です。" \
  -F "user_id=test-user" \
  https://your-domain.com/api/pronunciation-assessment
```

## 発音評価(base64を使用)

```bash
curl -X POST \
  -H "X-API-Key: your_api_key" \
  -H "Content-Type: application/json" \
  -H "X-Audio-Format: base64" \
  -d '{
    "audio_base64": "UklGRiSFAABXQVZFLAAAAAA=...",
    "reference_text": "こんにちは、私の名前は田中です。",
    "user_id": "test-user"
  }' \
  https://your-domain.com/api/pronunciation-assessment
```

## テキストを音声に変換する

```bash
curl -X POST \
  -H "X-API-Key: your_api_key" \
  -H "Content-Type: application/json" \
  -d '{"text":"こんにちは、私の名前は田中です。", "voice_name":"ja-JP-NanamiNeural"}' \
  --output speech.mp3 \
  https://your-domain.com/api/text-to-speech
```

## テキストからの意図の識別

```bash
curl -X POST \
  -H "X-API-Key: your_api_key" \
  -H "Content-Type: application/json" \
  -d '{"text":"こんにちは、初めまして。お願いします。", "user_id":"test-user"}' \
  https://your-domain.com/api/intent-recognition
```

## base64 オーディオから意図を特定する

```bash
curl -X POST \
  -H "X-API-Key: your_api_key" \
  -H "Content-Type: application/json" \
  -H "X-Audio-Format: base64" \
  -d '{
    "audio_base64": "UklGRiSFAABXQVZFLAAAAAA=...",
    "user_id": "test-user"
  }' \
  https://your-domain.com/api/intent-recognition
```

# APIテスト

`test-api.js` スクリプトを使用して API エンドポイントをテストします。

```bash
# すべてのAPIをテストする
node test-api.js --all

# 各APIを個別にテストする
node test-api.js --stt           # Speech to Text
node test-api.js --pronunciation # Pronunciation Assessment
node test-api.js --pronunciation-base64 # Pronunciation Assessment với base64
node test-api.js --tts           # Text to Speech
node test-api.js --intent        # Intent Recognition
node test-api.js --realtime      # Real-time Speech Recognition (WebSocket)
```

## 参考資料

- [Azure Speech SDK のドキュメント](https://learn.microsoft.com/en-us/javascript/api/microsoft-cognitiveservices-speech-sdk/)
- [発音評価 API ガイド](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/rest-speech-to-text#pronunciation-assessment-parameters)

