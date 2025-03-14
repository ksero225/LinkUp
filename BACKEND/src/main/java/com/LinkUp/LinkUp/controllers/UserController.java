package com.LinkUp.LinkUp.controllers;

import com.LinkUp.LinkUp.domain.UserLoginRequest;
import com.LinkUp.LinkUp.domain.UserRegisterRequest;
import com.LinkUp.LinkUp.domain.documents.User;
import com.LinkUp.LinkUp.domain.dtos.ContactDto;
import com.LinkUp.LinkUp.domain.dtos.UserDto;
import com.LinkUp.LinkUp.domain.dtos.UserLoginRequestDto;
import com.LinkUp.LinkUp.domain.dtos.UserRegisterRequestDto;
import com.LinkUp.LinkUp.mappers.Mapper;
import com.LinkUp.LinkUp.mappers.impl.UserLoginRequestMapper;
import com.LinkUp.LinkUp.services.UserService;
import lombok.AllArgsConstructor;
import lombok.NoArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@AllArgsConstructor
@RequestMapping(path = "/api/users")
public class UserController {
    private UserService userService;
    private Mapper<User, UserDto> userMapper;
    private Mapper<UserLoginRequest, UserLoginRequestDto> userLoginRequestMapper;
    private Mapper<UserRegisterRequest, UserRegisterRequestDto> userRegisterRequestMapper;


    @GetMapping(path = "/test")
    public String welcomeMessage() {
        return "Siemano, działa ";
    }

    @GetMapping("/user")
    public ResponseEntity<UserDto> getUserOneById(@RequestParam(value = "userId") final String userId) {
        return userService.findOne(userId)
                .map(user -> {
                    UserDto userDto = userMapper.mapTo(user);
                    List<ContactDto> userFriends = userService.idListToContactList(user.getUserFriendList());
                    userDto.setUserFriendList(userFriends);
                    return ResponseEntity.ok(userDto);
                })
                .orElseGet(() ->
                        new ResponseEntity<>(HttpStatus.NOT_FOUND)
                );
    }

    @PostMapping(path = "/login")
    public ResponseEntity<UserDto> getUserByLogin(@RequestBody UserLoginRequestDto requestBody) {
        final UserLoginRequest userLoginRequest = userLoginRequestMapper.mapFrom(requestBody);

        return userService.loginUser(userLoginRequest)
                .map(user -> {
                    UserDto userDto = userMapper.mapTo(user);
                    List<ContactDto> userFriends = userService.idListToContactList(user.getUserFriendList());
                    userDto.setUserFriendList(userFriends);
                    return ResponseEntity.ok(userDto);
                })
                .orElseGet(() ->
                        new ResponseEntity<>(HttpStatus.NOT_FOUND)
                );
    }

    @PostMapping(path = "/register")
    public ResponseEntity<UserDto> registerUser(@RequestBody UserRegisterRequestDto requestBody) {
        final UserRegisterRequest userRegisterRequest = userRegisterRequestMapper.mapFrom(requestBody);

        User user = userService.registerUser(userRegisterRequest);

        user.setUserPassword("");
        return new ResponseEntity<>(userMapper.mapTo(user), HttpStatus.OK);
    }

    @PatchMapping(path = "/toggleStatus")
    public ResponseEntity<Void> toggleUserStatus(@RequestParam(value = "userId") final String userId) {
        userService.toggleUserStatus(userId);
        return new ResponseEntity<>(HttpStatus.OK);
    }

}
