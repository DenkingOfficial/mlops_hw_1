# MLOps homework #3

Team #2

Контейнеризация микросервисов МО

* Шершнев Андрей (РИМ-120907)
* Кожин Артём (РИМ-120906)
* Иванов Сергей (РИМ-120906)
* Чупахин Юрий (РИМ-120908)

Проект, использованный для запуска в контейнере: [cat_breed_classifier](https://github.com/DenkingOfficial/cat_breed_classifier)

Ссылка на DockerHub: https://hub.docker.com/repository/docker/denking/cat_breed_classifier/

Dockerfile из репозитория `cat_breed_classifier`:
```
FROM python:3.8
WORKDIR /cat_breed_classifier
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
WORKDIR /cat_breed_classifier/models
RUN curl -L https://www.dropbox.com/s/jqzwew182acdohn/cats_18_EfficientNetB0.h5 -o cats_18_EfficientNetB0.h5
WORKDIR /cat_breed_classifier
COPY . .
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host=0.0.0.0", "--reload"]
```

Чтобы собрать проект, отправить на DockerHub и запустить его используйте build.sh

При отправке на DockerHub присваивается тэг вида branch_commit

![image](https://user-images.githubusercontent.com/38957619/230889937-27267fb8-1a5a-466d-833b-ef4f65a5331b.png)
