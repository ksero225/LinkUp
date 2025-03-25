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
@Schema(description = "DTO for user login request containing credentials")
public class UserLoginRequestDto {

    @Schema(description = "User's login name", example = "john_doe")
    private String userLogin;

    @Schema(description = "User's password", example = "********")
    private String userPassword;
}
