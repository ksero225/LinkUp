package com.LinkUp.LinkUp.services;

import com.LinkUp.LinkUp.domain.UserLoginRequest;
import com.LinkUp.LinkUp.domain.UserRegisterRequest;
import com.LinkUp.LinkUp.domain.documents.User;
import com.LinkUp.LinkUp.domain.dtos.UserDto;
import org.springframework.http.ResponseEntity;

import javax.swing.text.html.Option;
import java.util.Optional;

public interface UserService {
    Optional<User> loginUser(UserLoginRequest userLoginRequest);

    User registerUser(UserRegisterRequest userRegisterRequest);

    Optional<User> findOne(String userId);

    void toggleUserStatus(String userId);
}
