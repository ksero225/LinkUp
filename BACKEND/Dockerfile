FROM openjdk:21-oracle
COPY BACKEND/target/*.jar test.jar
EXPOSE 8089
ENTRYPOINT ["java", "-jar","test.jar"]