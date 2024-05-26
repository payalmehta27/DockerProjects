FROM openjdk:11
WORKDIR app/
COPY javaapp/Hello.java  .
RUN javac Hello.java

CMD ["java","Hello"]  
