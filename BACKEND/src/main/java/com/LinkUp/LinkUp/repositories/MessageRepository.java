package com.LinkUp.LinkUp.repositories;

import com.LinkUp.LinkUp.domain.documents.Message;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface MessageRepository extends MongoRepository<Message, String> {
    Page<Message> findBySenderAndRecipientOrRecipientAndSender(
            String sender,
            String recipient,
            String recipient2,
            String sender2,
            Pageable pageable
    );
}
