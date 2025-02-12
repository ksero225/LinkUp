package com.LinkUp.LinkUp.mappers;

public interface Mapper<classA, classB> {
    classB mapTo(classA a);

    classA mapFrom(classB b);
}
