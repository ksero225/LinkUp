package com.LinkUp.LinkUp.repositories;

import com.LinkUp.LinkUp.domain.documents.User;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;
import org.springframework.data.mongodb.repository.Update;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;
import org.springframework.transaction.annotation.Transactional;

import java.util.Optional;

@Repository
public interface UserRepository extends MongoRepository<User, String> {
    Optional<User> findUserByUserLogin(String userLogin);

    boolean existsUserByUserLogin(String userLogin);
    boolean existsUserByUserEmail(String userEmail);

    //boolean existsByUserId(String userId);
}
