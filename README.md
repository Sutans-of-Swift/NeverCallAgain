# NeverCallAgain

Project for Hacknotts2020

Substitute for phonecalls for really awkward people.

*Magic of AI*

### Text to Voice
- Twilio parses text to extract target number and message
- Message sent to AWS Polly
- Polly produces audio file to S3 bucket
- Audio file piped back to twilio

### Voice to Text
Take anything spoken into the called phone and texts it back to the text sender.