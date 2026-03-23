FROM python:3.12-slim

WORKDIR /app

# встановлюємо uv
RUN pip install uv

# копіюємо тільки залежності
COPY pyproject.toml uv.lock ./

# встановлюємо залежності
RUN uv sync --frozen

# копіюємо весь проєкт
COPY . .

EXPOSE 3000

CMD ["uv", "run", "python", "app.py"]