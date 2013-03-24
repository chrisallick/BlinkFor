int incomingByte = 0;

void setup() {
    Serial.begin(9600);

    pinMode( 13, OUTPUT );
}

void loop() {
        if (Serial.available() > 0) {
                // read the incoming byte:
                incomingByte = Serial.read();

                // say what you got:
                Serial.print("I received: ");
                Serial.println(incomingByte, DEC);
                
                if( incomingByte == 119 ) {
                    digitalWrite( 13, HIGH );
                    delay( 500 );
                    digitalWrite( 13, LOW );
                }
        }
}
