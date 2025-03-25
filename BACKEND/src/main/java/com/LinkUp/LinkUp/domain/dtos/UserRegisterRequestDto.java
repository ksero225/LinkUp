package com.LinkUp.LinkUp.domain.dtos;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
@Builder
public class UserRegisterRequestDto {
    private String userLogin;
    private String userPassword;
    private String userEmail;
    private String userPublicKey;
}
