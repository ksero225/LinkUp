package com.LinkUp.LinkUp.domain.dtos;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class ContactDto {
    private String contactId;
    private String contactLogin;
    private String contactEmail;
    private boolean isUserActive;
}
