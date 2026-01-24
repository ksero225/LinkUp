FROM eclipse-temurin:21-jre
COPY BACKEND/target/*.jar app.jar
CMD ["sh", "-c", "java -Dserver.port=${PORT:-8089} -jar app.jar"]
