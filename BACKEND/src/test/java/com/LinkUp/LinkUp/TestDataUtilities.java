package com.LinkUp.LinkUp;


import com.LinkUp.LinkUp.domain.documents.User;
import org.springframework.data.annotation.Id;

import java.util.ArrayList;
import java.util.List;

public class TestDataUtilities {

    public static User createTestUserA() {
        return User.builder()
                .userId("A")
                .userLogin("loginA")
                .userPassword("passwordA")
                .userEmail("emailA")
                .isUserActive(true)
                .userFriendList(new ArrayList<>())
                .build();
    }

    public static User createTestUserB() {
        return User.builder()
                .userId("B")
                .userLogin("loginB")
                .userPassword("passwordB")
                .userEmail("emailB")
                .isUserActive(true)
                .userFriendList(new ArrayList<>())
                .build();
    }

    public static User createTestUserC() {
        return User.builder()
                .userId("C")
                .userLogin("loginC")
                .userPassword("passwordC")
                .userEmail("emailC")
                .isUserActive(true)
                .userFriendList(new ArrayList<>())
                .build();
    }
}
