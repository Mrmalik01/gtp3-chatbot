# GPT3-chatbot 🚀
A SMS-based chatbot engine built using the GPT3 Language model. It allows users to chat with an AI machine through SMS. 

# instructions 
1. Clone the git repository or download the ZIP file.
1. Get the access token from the OpenAI - https://beta.openai.com/  
2. Create a file called .env in your root directory and insert the code you received from the OpenAI
```bash
OPENAI_KEY=<your_secret_key>
```
3. Create a trial account in twilio to get a registered phone number. 
4. After creating the account, purchase a phone number. 
5. Install relevant files by typing the following command in your terminal
```bash
pip install twilio openai python-dotenv flask ngrok 
```
6. Run the application
```bash
python app.py
```
7. As your application is running on a local server, it is not reachable by the twilio server. To fix this, open another terminal and then type the following command in your terminal
```bash
ngrok http 5000
```
8. Copy the forwarding url present in the terminal and go to your twilio console. Then click on your phone number and scroll down to the messaging section.
9. In the 'A MESSAGE COMES IN" webhook, paste your forwarding url. 
10. Start sending SMS to your newly authorised phone number. 

## Contact 🚀
If you have any questions, feel free to reach out. My contact details are on my profile. 

#happyCoding #GTP3Engine
