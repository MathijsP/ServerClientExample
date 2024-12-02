from fastapi import FastAPI
import uvicorn
import models
import logging

app = FastAPI()

USER_TOKEN_DICT = {"mathijs@mail.com": "00112233", "some_guy@mail.com": "123456789"}

logger = logging.getLogger("fast")


def is_user_valid(user: models.User) -> bool:
    # Authenticate user.
    stored_token = USER_TOKEN_DICT.get(user.user_name)
    return user.token == stored_token


@app.post("/work")
async def do_work(inputs: models.Inputs):
    """
    This function can do the fancy calculation and return outputs.
    """
    logger.info(f"received request - {inputs}")
    # Validate the user and token.
    if not is_user_valid(inputs.user):
        return {}

    # Do fancy calculation and send a response.
    return {inputs.user.user_name: [100, 10000, 100000], "other_data": [2, 22, 222]}


def main():
    # Start the server.
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
