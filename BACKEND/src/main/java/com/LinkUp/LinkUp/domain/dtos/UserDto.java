package com.LinkUp.LinkUp.domain.dtos;

import io.swagger.v3.oas.annotations.media.Schema;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.List;

@Data
@AllArgsConstructor
@NoArgsConstructor
@Builder
@Schema(description = "DTO representing a registered user with profile details and friend list")
public class UserDto {

    @Schema(description = "Unique identifier of the user", example = "64b5f2e8c3a5d9e123456789")
    private String userId;

    @Schema(description = "User's login name", example = "john_doe")
    private String userLogin;

    @Schema(description = "User's password (should be stored hashed in a real-world application)", example = "********")
    private String userPassword;

    @Schema(description = "User's email address", example = "john.doe@example.com")
    private String userEmail;

    @Schema(description = "Indicates whether the user account is active", example = "true")
    private boolean isUserActive;

    @Schema(description = "User's public key for secure communication", example = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA...")
    private String userPublicKey;

    @Schema(description = "List of contacts representing the user's friend list")
    private List<ContactDto> userFriendList;
}
