package com.LinkUp.LinkUp.mappers.impl;

import com.LinkUp.LinkUp.domain.documents.User;
import com.LinkUp.LinkUp.domain.dtos.ContactDto;
import com.LinkUp.LinkUp.domain.dtos.UserDto;
import com.LinkUp.LinkUp.mappers.Mapper;
import org.springframework.stereotype.Component;

import java.util.stream.Collectors;

@Component
public class UserMapper implements Mapper<User, UserDto> {
    @Override
    public UserDto mapTo(User user) {
        return UserDto.builder()
                .userId(user.getUserId())
                .userLogin(user.getUserLogin())
                .userPassword(user.getUserPassword())
                .userEmail(user.getUserEmail())
                .isUserActive(user.isUserActive())
                .build();
    }

    @Override
    public User mapFrom(UserDto userDto) {
        return User.builder()
                .userId(userDto.getUserId())
                .userLogin(userDto.getUserLogin())
                .userPassword(userDto.getUserPassword())
                .userEmail(userDto.getUserEmail())
                .isUserActive(userDto.isUserActive())
                .build();
    }
}
