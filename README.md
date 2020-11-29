# NeverCallAgain

Project for Hacknotts2020.

Substitute for phonecalls for really awkward people.

Uses the _magic of AI_.

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

## During HackBotts2020 use it by texting:
`+44 7411 226037`

The First line should be the phone number you want to call, and the rest of the message is read aloud.
