FROM ohshin/ubot:dev

WORKDIR ls/app 


COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "-m", "PyroUbot"]
