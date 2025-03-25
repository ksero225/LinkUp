package com.LinkUp.LinkUp.domain.dtos;

import io.swagger.v3.oas.annotations.media.Schema;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
@Builder
@Schema(description = "DTO for user registration request containing credentials and public key")
public class UserRegisterRequestDto {

    @Schema(description = "User's chosen login name", example = "john_doe")
    private String userLogin;

    @Schema(description = "User's chosen password", example = "********")
    private String userPassword;

    @Schema(description = "User's email address", example = "john.doe@example.com")
    private String userEmail;

    @Schema(description = "User's public key for secure communication", example = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA...")
    private String userPublicKey;
}
