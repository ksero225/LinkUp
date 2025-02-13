package com.LinkUp.LinkUp.services.implementations;

import com.LinkUp.LinkUp.domain.UserLoginRequest;
import com.LinkUp.LinkUp.domain.UserRegisterRequest;
import com.LinkUp.LinkUp.domain.documents.User;
import com.LinkUp.LinkUp.repositories.UserRepository;
import com.LinkUp.LinkUp.services.UserService;
import lombok.AllArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.web.server.ResponseStatusException;

import java.util.Optional;

@Service
@AllArgsConstructor
public class UserServiceImpl implements UserService {
    private final UserRepository userRepository;

    @Override
    public Optional<User> findOne(String userId) {
        return userRepository.findById(userId);
    }

    @Override
    public Optional<User> loginUser(UserLoginRequest userLoginRequest) {
        User user = userRepository.findUserByUserLogin(userLoginRequest.getUserLogin())
                .orElseThrow(() -> new ResponseStatusException(HttpStatus.NOT_FOUND, "Invalid login. User not found"));

        if (!user.getUserPassword().equals(userLoginRequest.getUserPassword())) {
            throw new ResponseStatusException(HttpStatus.UNAUTHORIZED, "Invalid password.");
        }

        user.setUserPassword("");

        userRepository.toggleUserStatus(user.getUserId());

        return Optional.of(user);
    }

    @Override
    public User registerUser(UserRegisterRequest userRegisterRequest) {

        if (userRepository.existsByUserLoginOrUserEmail(userRegisterRequest.getUserLogin(), userRegisterRequest.getUserEmail())) {
            throw new ResponseStatusException(HttpStatus.CONFLICT, "Login or email is already taken.");
        }

        User newUser = User.builder()
                .userLogin(userRegisterRequest.getUserLogin())
                .userPassword(userRegisterRequest.getUserPassword())
                .userEmail(userRegisterRequest.getUserEmail())
                .build();

        return userRepository.save(newUser);
    }

    @Override
    @Transactional
    public void toggleUserStatus(String userId) {
        if(!userRepository.existsByUserId(userId)){
            throw new ResponseStatusException(HttpStatus.NOT_FOUND, "User not found.");
        }

        userRepository.toggleUserStatus(userId);
    }
}
