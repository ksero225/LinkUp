package com.LinkUp.LinkUp.domain.documents;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
@Document
public class User {
    @Id
    private String userId;
    private String userLogin;
    private String userPassword;
    private String userEmail;
    private Boolean isUserActive;
}
