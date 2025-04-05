package com.LinkUp.LinkUp.domain.documents;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import java.time.LocalDateTime;

@Data
@AllArgsConstructor
@NoArgsConstructor
@Builder
@Document(collection = "message_history")
public class Message {
    @Id
    private String id;
    private String sender;
    private String recipient;
    private String encryptedMessage;
    private String iv;
    private String keyForRecipient;
    private String keyForSender;
    private LocalDateTime timestamp;
}
