package com.LinkUp.LinkUp.mappers.impl;

import com.LinkUp.LinkUp.domain.UserLoginRequest;
import com.LinkUp.LinkUp.domain.dtos.UserLoginRequestDto;
import com.LinkUp.LinkUp.mappers.Mapper;
import org.springframework.stereotype.Component;

@Component
public class UserLoginRequestMapper implements Mapper<UserLoginRequest, UserLoginRequestDto> {
    @Override
    public UserLoginRequestDto mapTo(UserLoginRequest userLoginRequest) {
        return UserLoginRequestDto.builder()
                .userLogin(userLoginRequest.getUserLogin())
                .userPassword(userLoginRequest.getUserPassword())
                .build();
    }

    @Override
    public UserLoginRequest mapFrom(UserLoginRequestDto userLoginRequestDto) {
        return UserLoginRequest.builder()
                .userLogin(userLoginRequestDto.getUserLogin())
                .userPassword(userLoginRequestDto.getUserPassword())
                .build();
    }
}
