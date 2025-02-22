package com.LinkUp.LinkUp.controllers;

import com.LinkUp.LinkUp.domain.documents.User;
import com.LinkUp.LinkUp.domain.dtos.ContactDto;
import com.LinkUp.LinkUp.domain.dtos.UserDto;
import com.LinkUp.LinkUp.mappers.Mapper;
import com.LinkUp.LinkUp.services.UserService;
import lombok.AllArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PatchMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@AllArgsConstructor
@RequestMapping(path = "/api/friendList")
public class UserFriendListController {
    private UserService userService;

    @PatchMapping(path = "/add")
    public ResponseEntity<List<ContactDto>> addContactToFriendList(
            @RequestParam(value = "userId") String userId,
            @RequestParam(value = "contactId") String contactId
    ) {
        return new ResponseEntity<>(userService.addContact(userId, contactId), HttpStatus.OK);
    }

    @PatchMapping(path = "/delete")
    public ResponseEntity<List<ContactDto>> deleteContactFromFriendList(
            @RequestParam(value = "userId") String userId,
            @RequestParam(value = "contactId") String contactId
    ) {
        return new ResponseEntity<>(userService.deleteContact(userId, contactId), HttpStatus.OK);
    }


}
