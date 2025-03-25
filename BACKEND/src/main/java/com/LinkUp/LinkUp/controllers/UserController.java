package com.LinkUp.LinkUp.controllers;

import com.LinkUp.LinkUp.domain.UserLoginRequest;
import com.LinkUp.LinkUp.domain.UserRegisterRequest;
import com.LinkUp.LinkUp.domain.documents.User;
import com.LinkUp.LinkUp.domain.dtos.ContactDto;
import com.LinkUp.LinkUp.domain.dtos.UserDto;
import com.LinkUp.LinkUp.domain.dtos.UserLoginRequestDto;
import com.LinkUp.LinkUp.domain.dtos.UserRegisterRequestDto;
import com.LinkUp.LinkUp.mappers.Mapper;
import com.LinkUp.LinkUp.services.UserService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.Parameter;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.tags.Tag;
import lombok.AllArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@AllArgsConstructor
@RequestMapping(path = "/api/users")
@Tag(name = "Users", description = "API for user management.")
public class UserController {
    private UserService userService;
    private Mapper<User, UserDto> userMapper;
    private Mapper<UserLoginRequest, UserLoginRequestDto> userLoginRequestMapper;
    private Mapper<UserRegisterRequest, UserRegisterRequestDto> userRegisterRequestMapper;

    @GetMapping(path = "/test")
    @Operation(
            summary = "Welcome message",
            description = "A test endpoint that returns a simple confirmation message."
    )
    public String welcomeMessage() {
        return "Hello, it's working!";
    }

    @GetMapping("/user")
    @Operation(
            summary = "Get user by ID",
            description = "Retrieves user details based on the provided user ID."
    )
    public ResponseEntity<UserDto> getUserOneById(
            @Parameter(description = "Unique identifier of the user", example = "64b5f2e8c3a5d9e123456789")
            @RequestParam(value = "userId") final String userId) {
        return userService.findOne(userId)
                .map(this::buildUserDto)
                .map(ResponseEntity::ok)
                .orElseGet(() -> new ResponseEntity<>(HttpStatus.NOT_FOUND));
    }

    @PostMapping(path = "/login")
    @Operation(
            summary = "User login",
            description = "Authenticates the user with provided credentials and returns user data along with the friend list."
    )
    public ResponseEntity<UserDto> getUserByLogin(
            @io.swagger.v3.oas.annotations.parameters.RequestBody(
                    description = "User login credentials",
                    required = true
            )
            @RequestBody UserLoginRequestDto requestBody) {
        final UserLoginRequest userLoginRequest = userLoginRequestMapper.mapFrom(requestBody);
        return userService.loginUser(userLoginRequest)
                .map(this::buildUserDto)
                .map(ResponseEntity::ok)
                .orElseGet(() -> new ResponseEntity<>(HttpStatus.NOT_FOUND));
    }

    @PostMapping(path = "/register")
    @Operation(
            summary = "User registration",
            description = "Registers a new user and returns the user data (password is omitted for security)."
    )
    public ResponseEntity<UserDto> registerUser(
            @io.swagger.v3.oas.annotations.parameters.RequestBody(
                    description = "User registration data",
                    required = true
            )
            @RequestBody UserRegisterRequestDto requestBody) {
        final UserRegisterRequest userRegisterRequest = userRegisterRequestMapper.mapFrom(requestBody);
        User user = userService.registerUser(userRegisterRequest);

        user.setUserPassword("");

        return new ResponseEntity<>(userMapper.mapTo(user), HttpStatus.OK);
    }

    @PatchMapping(path = "/toggleStatus")
    @Operation(
            summary = "Toggle user status",
            description = "Switches the user's active status between active and inactive."
    )
    public ResponseEntity<Void> toggleUserStatus(
            @Parameter(description = "Unique identifier of the user", example = "64b5f2e8c3a5d9e123456789")
            @RequestParam(value = "userId") final String userId) {
        userService.toggleUserStatus(userId);
        return new ResponseEntity<>(HttpStatus.OK);
    }

    private UserDto buildUserDto(User user) {
        UserDto dto = userMapper.mapTo(user);
        dto.setUserFriendList(userService.idListToContactList(user.getUserFriendList()));
        return dto;
    }
}
