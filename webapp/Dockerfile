FROM node:14.7.0-buster-slim
MAINTAINER zacronan@naver.com

# pm2 설치
RUN npm install -g pm2

# production 환경 설정
ENV NODE_ENV production
RUN mkdir -p /app

WORKDIR /app

# 앱 의존성 설치
# 가능한 경우(npm@5+) package.json과 package-lock.json을 모두 복사하기 위해
# 와일드카드를 사용
COPY package*.json ./
RUN npm install

# 앱 소스 추가
COPY . .

## Start the service
CMD ["pm2-docker", "run.json"]