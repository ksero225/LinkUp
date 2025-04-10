package com.LinkUp.LinkUp.controllers;

import com.LinkUp.LinkUp.domain.dtos.ContactDto;
import com.LinkUp.LinkUp.domain.enums.ContactOperation;
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

    @PatchMapping
    @Operation(
            summary = "Update friend list",
            description = "Adds or removes a contact from the user's friend list based on the specified operation."
    )
    public ResponseEntity<List<ContactDto>> updateFriendList(
            @Parameter(description = "Unique login of the user", example = "test")
            @RequestParam(value = "userLogin") String userLogin,
            @Parameter(description = "Unique login of the contact", example = "test2")
            @RequestParam(value = "contactLogin") String contactLogin,
            @Parameter(description = "Operation to perform: ADD or DELETE", example = "ADD")
            @RequestParam(value = "operation") ContactOperation operation) {
        return new ResponseEntity<>(userService.updateContact(userLogin, contactLogin, operation), HttpStatus.OK);
    }
}
