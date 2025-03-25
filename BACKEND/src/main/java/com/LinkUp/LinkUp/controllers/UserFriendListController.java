package com.LinkUp.LinkUp.controllers;

import com.LinkUp.LinkUp.domain.dtos.ContactDto;
import com.LinkUp.LinkUp.services.UserService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.Parameter;
import io.swagger.v3.oas.annotations.tags.Tag;
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
@Tag(name = "Friend list", description = "API for managing the user's friend list.")
public class UserFriendListController {
    private UserService userService;

    @PatchMapping(path = "/add")
    @Operation(
            summary = "Add contact to friend list",
            description = "Adds a contact to the user's friend list."
    )
    public ResponseEntity<List<ContactDto>> addContactToFriendList(
            @Parameter(description = "Unique identifier of the user", example = "64b5f2e8c3a5d9e123456789")
            @RequestParam(value = "userId") String userId,
            @Parameter(description = "Unique identifier of the contact to add", example = "64b5f2e8c3a5d9e987654321")
            @RequestParam(value = "contactId") String contactId) {
        return new ResponseEntity<>(userService.addContact(userId, contactId), HttpStatus.OK);
    }

    @PatchMapping(path = "/delete")
    @Operation(
            summary = "Delete contact from friend list",
            description = "Removes a contact from the user's friend list."
    )
    public ResponseEntity<List<ContactDto>> deleteContactFromFriendList(
            @Parameter(description = "Unique identifier of the user", example = "64b5f2e8c3a5d9e123456789")
            @RequestParam(value = "userId") String userId,
            @Parameter(description = "Unique identifier of the contact to delete", example = "64b5f2e8c3a5d9e987654321")
            @RequestParam(value = "contactId") String contactId) {
        return new ResponseEntity<>(userService.deleteContact(userId, contactId), HttpStatus.OK);
    }
}
