package com.LinkUp.LinkUp.domain.dtos;

import io.swagger.v3.oas.annotations.media.Schema;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
@Schema(description = "DTO representing a user contact in the friend list")
public class ContactDto {

    @Schema(description = "Unique identifier of the contact", example = "64b5f2e8c3a5d9e123456789")
    private String contactId;

    @Schema(description = "Login (username) of the contact", example = "john_doe")
    private String contactLogin;

    @Schema(description = "Email address of the contact", example = "john.doe@example.com")
    private String contactEmail;

    @Schema(description = "Indicates if the contact is currently active", example = "true")
    private boolean isUserActive;

    @Schema(description = "Public key of the user for secure communication", example = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA...")
    private String userPublicKey;
}
