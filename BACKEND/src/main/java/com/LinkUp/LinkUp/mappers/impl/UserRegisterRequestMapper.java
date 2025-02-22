package com.LinkUp.LinkUp.mappers.impl;

import com.LinkUp.LinkUp.domain.UserRegisterRequest;
import com.LinkUp.LinkUp.domain.dtos.UserRegisterRequestDto;
import com.LinkUp.LinkUp.mappers.Mapper;
import org.springframework.stereotype.Component;

@Component
public class UserRegisterRequestMapper implements Mapper<UserRegisterRequest, UserRegisterRequestDto> {
    @Override
    public UserRegisterRequestDto mapTo(UserRegisterRequest userRegisterRequest) {
        return UserRegisterRequestDto.builder()
                .userLogin(userRegisterRequest.getUserLogin())
                .userPassword(userRegisterRequest.getUserPassword())
                .userEmail(userRegisterRequest.getUserEmail())
                .build();
    }

    @Override
    public UserRegisterRequest mapFrom(UserRegisterRequestDto userRegisterRequestDto) {
        return UserRegisterRequest.builder()
                .userLogin(userRegisterRequestDto.getUserLogin())
                .userPassword(userRegisterRequestDto.getUserPassword())
                .userEmail(userRegisterRequestDto.getUserEmail())
                .build();
    }
}
