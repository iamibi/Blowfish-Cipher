void blowfishInitialise(BLOWFISH *blf, char *key, int keylen)
{
    int i, j, k;
    unsigned long int data, data_l, data_r;

    //Initialise the array of S in blf
    for (i = 0; i < 4; i++)
        for (j = 0; j < 256; j++)
            blf -> S[i][j] = S_Arr[i];

    j = 0;
    for (i = 0; i < N + 2; i++)
    {
        //set the data value to hex 0
        data = 0x00000000;
        for (k = 0; k < 4; k++)
        {
            data = (data << 8) | key[j];
            j = j + 1;

            //wrap the key value, if j reaches the end of key size
            if (j >= keylen)
                j = 0;
        }
        blf -> P[i] = P_Arr[i] ^ data;
    }

    data_l = data_r = 0x00000000;

    for (i = 0; i < 4; i++)
    {
        encryptMessage(blf, &data_l, &data_r);
        blf -> P[i] = data_l;
        blf -> P[i+1] = data_r;
    }

    for (i = 0; i < 4; i++)
    {
        for (j = 0; j < 256; j = j + 2)
        {
            encryptMessage(blf, &data_l, &data_r);
            blf -> S[i][j] = data_l;
            blf -> S[i][j+1] = data_r;
        }
    }
}
