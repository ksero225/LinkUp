package com.LinkUp.LinkUp.services;

import com.LinkUp.LinkUp.domain.UserLoginRequest;
import com.LinkUp.LinkUp.domain.UserRegisterRequest;
import com.LinkUp.LinkUp.domain.documents.User;

import java.util.Optional;

public interface UserService {
    Optional<User> loginUser(UserLoginRequest userLoginRequest);

    User registerUser(UserRegisterRequest userRegisterRequest);

}
