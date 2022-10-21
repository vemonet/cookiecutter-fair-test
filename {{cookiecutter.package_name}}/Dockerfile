FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9


WORKDIR /app/

COPY . /app

RUN pip install --upgrade pip

RUN pip install .

# Allow installing dev dependencies to run tests
ARG INSTALL_DEV=false
RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then pip install .[test,dev] ; fi"


# Run the API as non-root user for better security
# Create non root user 'app'
RUN addgroup --system app && adduser --system --group app
# Make sure all files belongs to the app user
RUN chown -R app:app /app && \
    chown -R app:app $HOME

USER app

ENV APP_MODULE=main:app
ENV PORT=8000
ENV PYTHONUNBUFFERED 1
# Ensures that the python output is sent straight to terminal to see it in real time:
