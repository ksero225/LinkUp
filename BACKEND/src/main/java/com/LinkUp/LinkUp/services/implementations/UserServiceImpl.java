package com.LinkUp.LinkUp.services.implementations;

import com.LinkUp.LinkUp.domain.UserLoginRequest;
import com.LinkUp.LinkUp.domain.UserRegisterRequest;
import com.LinkUp.LinkUp.domain.documents.User;
import com.LinkUp.LinkUp.domain.dtos.ContactDto;
import com.LinkUp.LinkUp.domain.enums.ContactOperation;
import com.LinkUp.LinkUp.repositories.UserRepository;
import com.LinkUp.LinkUp.services.UserService;
import lombok.AllArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.web.server.ResponseStatusException;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

@Service
@AllArgsConstructor
public class UserServiceImpl implements UserService {
    private final UserRepository userRepository;
    private final PasswordEncoder encoder;

    @Override
    public Optional<User> findOne(String userId) {
        return userRepository.findById(userId);
    }

    @Override
    public Optional<User> loginUser(UserLoginRequest userLoginRequest) {
        User foundUser = userRepository.findUserByUserLogin(userLoginRequest.getUserLogin())
                .orElseThrow(() -> new ResponseStatusException(
                                HttpStatus.NOT_FOUND,
                                "Invalid login. User not found"
                        )
                );

        if (!encoder.matches(userLoginRequest.getUserPassword(), foundUser.getUserPassword())) {
            throw new ResponseStatusException(HttpStatus.UNAUTHORIZED, "Invalid password.");
        }

        foundUser.setUserPassword("");

        toggleUserStatus(foundUser.getUserId());

        return Optional.of(foundUser);
    }

    @Override
    public User registerUser(UserRegisterRequest userRegisterRequest) {
        if (userRepository.existsUserByUserLogin(userRegisterRequest.getUserLogin())) {
            throw new ResponseStatusException(
                    HttpStatus.CONFLICT,
                    "Login is already taken."
            );
        }

        if (userRepository.existsUserByUserEmail(userRegisterRequest.getUserEmail())) {
            throw new ResponseStatusException(
                    HttpStatus.CONFLICT,
                    "email is already taken."
            );

        }

        User newUser = User.builder()
                .userLogin(userRegisterRequest.getUserLogin())
                .userPassword(encoder.encode(userRegisterRequest.getUserPassword()))
                .userEmail(userRegisterRequest.getUserEmail())
                .isUserActive(false)
                .userFriendList(new ArrayList<>())
                .userPublicKey(userRegisterRequest.getUserPublicKey())
                .build();

        return userRepository.save(newUser);
    }

    @Override
    public void toggleUserStatus(String userId) {
        User user = userRepository.findById(userId)
                .orElseThrow(() -> new ResponseStatusException(HttpStatus.NOT_FOUND, "User not found."));

        user.setUserActive(!user.isUserActive());

        userRepository.save(user);
    }

    @Override
    public List<ContactDto> updateContact(String userLogin, String contactLogin, ContactOperation operation) {
        if (userLogin.equals(contactLogin)) {
            throw new ResponseStatusException(HttpStatus.BAD_REQUEST, "You cannot add or remove yourself.");
        }

        User foundUser = userRepository.findUserByUserLogin(userLogin)
                .orElseThrow(() -> new ResponseStatusException(HttpStatus.NOT_FOUND, "User not found."));

        User foundContact = userRepository.findUserByUserLogin(contactLogin)
                .orElseThrow(() -> new ResponseStatusException(HttpStatus.NOT_FOUND, "Contact not found."));

        if (operation == ContactOperation.ADD) {
            if (foundUser.getUserFriendList().contains(foundContact.getUserId())) {
                throw new ResponseStatusException(
                        HttpStatus.CONFLICT,
                        "This contact is already in users friend list."
                );
            }
            foundUser.getUserFriendList().add(foundContact.getUserId());
            foundContact.getUserFriendList().add(foundUser.getUserId());
        } else if (operation == ContactOperation.DELETE) {
            if (!foundUser.getUserFriendList().contains(foundContact.getUserId())) {
                throw new ResponseStatusException(
                        HttpStatus.CONFLICT,
                        "This contact is not on your friend list."
                );
            }
            foundUser.getUserFriendList().remove(foundContact.getUserId());
            foundContact.getUserFriendList().remove(foundUser.getUserId());
        }

        userRepository.save(foundUser);
        userRepository.save(foundContact);

        return idListToContactList(foundUser.getUserFriendList());
    }

    @Override
    public List<ContactDto> idListToContactList(List<String> idList) {
        List<User> foundUsers = userRepository.findAllById(idList);

        return foundUsers.stream()
                .map(user -> new ContactDto(
                        user.getUserId(),
                        user.getUserLogin(),
                        user.getUserEmail(),
                        user.isUserActive(),
                        user.getUserPublicKey()
                )).collect(Collectors.toList());
    }

    private ContactDto mapFriendListIdsToContactDto(String contactId) {
        return userRepository.findById(contactId)
                .map(user -> new ContactDto(
                        user.getUserId(),
                        user.getUserLogin(),
                        user.getUserEmail(),
                        user.isUserActive(),
                        user.getUserPublicKey()
                )).orElse(null);
    }
}
