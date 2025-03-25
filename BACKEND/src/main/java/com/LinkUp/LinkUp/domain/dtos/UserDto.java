package com.LinkUp.LinkUp.domain.dtos;

import com.LinkUp.LinkUp.domain.documents.User;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.List;

@Data
@AllArgsConstructor
@NoArgsConstructor
@Builder
public class UserDto {
    private String userId;
    private String userLogin;
    private String userPassword;
    private String userEmail;
    private boolean isUserActive;
    private String userPublicKey;
    private List<ContactDto> userFriendList;
}
