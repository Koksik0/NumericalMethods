#Plik makefile
DIR = $(notdir $(CURDIR))

Name1 = NUM1aFloat
Name2 = NUM1aDouble
Name3 = NUM1bFloat
Name4 = NUM1bDouble

Exec1 = $(Name1)
Objs1 = $(Name1).o

Exec2 = $(Name2)
Objs2 = $(Name2).o

Exec3 = $(Name3)
Objs3 = $(Name3).o

Exec4 = $(Name4)
Objs4 = $(Name4).o

Coflags =  -Wall -std=gnu99 -pedantic -lm
Ldflags =  -Wall -std=gnu99 -pedantic -lm
CO = gcc
LD = $(CO)

%.o: %.c
	$(CO) $(Coflags) -c $< 

.Phony: $(Exec1)
$(Exec1): $(Objs1)
	$(LD) -o $@ $(Name1).c $(Ldflags)
$(Exec2): $(Objs2)
	$(LD) -o $@ $(Name2).c $(Ldflags)
$(Exec3): $(Objs3)
	$(LD) -o $@ $(Name3).c $(Ldflags)
$(Exec4): $(Objs4)
	$(LD) -o $@ $(Name4).c $(Ldflags)

aFloat: $(Exec1)
	./$(Exec1)
	./rysowanie$(Exec1)
aDouble: $(Exec2) 
	./$(Exec2)
	./rysowanie$(Exec2) 
bFloat: $(Exec3) 
	./$(Exec3)
	./rysowanie$(Exec3) 
bDouble: $(Exec4) 
	./$(Exec4)
	./rysowanie$(Exec4)

clean:
	rm -f *.o *.x *.*~ *~;
tar: clean
	(cd ../; tar -cvzf $(DIR).tar.gz $(DIR))