FROM python:3
WORKDIR /usr/src/app
COPY src/digit_to_words.py .
COPY src/digit_to_words_wrapper.sh .
RUN ["chmod", "+x", "digit_to_words_wrapper.sh"]
CMD [ "./digit_to_words_wrapper.sh" ]
