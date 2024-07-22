from flask import Flask, request
import base64
import logging
import pickle


app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/save_key', methods=['GET'])
def save_key():
    # Log that the endpoint has been hit
    app.logger.debug('Endpoint /save_key hit')
    
    # Get the token from the query parameters
    token = request.args.get('token')
    if token:
        # Log the received token
        app.logger.debug(f'Received token: {token}')
        
        try:
            # Decode the token to get the encryption key
            encryption_key = base64.urlsafe_b64decode(token.encode()).decode()
            # Log the decoded encryption key
            app.logger.debug(f'Decoded encryption key: {encryption_key}')
            

            #Unique identifier put at the end of token
            split = encryption_key.split('+n')
            identify = split[1]
            key = split[0]
            if identify:
                print(identify)
                
                print(0)
                # Use re.sub() to replace the characters with an empty string
              
                print(1)
                # Save the encryption key (for example, save to a file or database)
                with open(f'encry.pickle_encryptionkey_{identify}', 'wb') as file:
                    pickle.dump(key, file)
                    # Log that the key has been saved
                    app.logger.debug('Encryption key saved to encryption_key.txt')
                    
                return "Encryption key saved successfully!"
        except Exception as e:
            app.logger.error(f'Error decoding token or saving encryption key: {e}')
            return "Error processing token", 500
    else:
        app.logger.error('No token or ID provided')
        return "No token or ID provided", 400
    


if __name__ == '__main__':
    app.run(debug=True)
