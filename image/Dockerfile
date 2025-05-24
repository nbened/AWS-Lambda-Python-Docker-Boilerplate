FROM public.ecr.aws/lambda/python:3.11

# Copy requirements.txt
COPY requirements.txt ${LAMBDA_TASK_ROOT}

# Install the specified packages
RUN pip install -r requirements.txt

# Copy all files in ./src (including subdirectories. if you just want in src, use COPY src/* ${LAMBDA_TASK_ROOT}
COPY src ${LAMBDA_TASK_ROOT}

# Set the CMD to your handler
CMD ["app.handler"]
