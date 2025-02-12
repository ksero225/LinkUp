FROM openjdk:21-oracle
COPY target/*.jar test.jar
EXPOSE 8089
ENTRYPOINT ["java", "-jar","test.jar"]