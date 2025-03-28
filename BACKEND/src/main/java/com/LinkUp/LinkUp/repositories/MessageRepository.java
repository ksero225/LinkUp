package com.LinkUp.LinkUp.repositories;

import com.LinkUp.LinkUp.domain.documents.Message;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;
import org.springframework.stereotype.Repository;

@Repository
public interface MessageRepository extends MongoRepository<Message, String> {
    @Query("{ $or: [ { sender: ?0, recipient: ?1 }, { sender: ?1, recipient: ?0 } ] }")
    Page<Message> findBySenderAndRecipientOrRecipientAndSender(
            String sender,
            String recipient,
            Pageable pageable
    );
}
