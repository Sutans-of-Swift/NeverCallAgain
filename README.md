# NeverCallAgain

Project for Hacknotts2020

Substitute for phonecalls for really awkward people.

Uses the *magic of AI*.

### Text to Voice
- Twilio parses text to extract target number and message
- Message sent to AWS Polly
- Polly produces audio file to S3 bucket
- Audio file piped back to twilio

Message format:
```
5555 555 5555
This is a message I want to be
spoken aloud to the number on
the first line.
```

### Voice to Text
Take anything spoken into the called phone and texts it back to the text sender.