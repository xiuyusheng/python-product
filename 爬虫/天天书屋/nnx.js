function ajax(xxyyu) {
    function RotateLeft(lValue, iShiftBits) {
        return (lValue << iShiftBits) | (lValue >>> (32 - iShiftBits))
    }
    function AddUnsigned(lX, lY) {
        var lX4, lY4, lX8, lY8, lResult;
        lX8 = (lX & 0x80000000);
        lY8 = (lY & 0x80000000);
        lX4 = (lX & 0x40000000);
        lY4 = (lY & 0x40000000);
        lResult = (lX & 0x3FFFFFFF) + (lY & 0x3FFFFFFF);
        if (lX4 & lY4)
            return (lResult ^ 0x80000000 ^ lX8 ^ lY8);
        if (lX4 | lY4) {
            if (lResult & 0x40000000)
                return (lResult ^ 0xC0000000 ^ lX8 ^ lY8);
            else
                return (lResult ^ 0x40000000 ^ lX8 ^ lY8)
        } else
            return (lResult ^ lX8 ^ lY8)
    }
    function F(x, y, z) {
        return (x & y) | ((~x) & z)
    }
    function G(x, y, z) {
        return (x & z) | (y & (~z))
    }
    function H(x, y, z) {
        return (x ^ y ^ z)
    }
    function I(x, y, z) {
        return (y ^ (x | (~z)))
    }
    function FF(a, b, c, d, x, s, ac) {
        a = AddUnsigned(a, AddUnsigned(AddUnsigned(F(b, c, d), x), ac));
        return AddUnsigned(RotateLeft(a, s), b)
    }
    function GG(a, b, c, d, x, s, ac) {
        a = AddUnsigned(a, AddUnsigned(AddUnsigned(G(b, c, d), x), ac));
        return AddUnsigned(RotateLeft(a, s), b)
    }
    function HH(a, b, c, d, x, s, ac) {
        a = AddUnsigned(a, AddUnsigned(AddUnsigned(H(b, c, d), x), ac));
        return AddUnsigned(RotateLeft(a, s), b)
    }
    function II(a, b, c, d, x, s, ac) {
        a = AddUnsigned(a, AddUnsigned(AddUnsigned(I(b, c, d), x), ac));
        return AddUnsigned(RotateLeft(a, s), b)
    }
    function ConvertToWordArray(xxyyu) {
        var lWordCount;
        var lMessageLength = xxyyu.length;
        var lNumberOfWords_temp1 = lMessageLength + 8;
        var lNumberOfWords_temp2 = (lNumberOfWords_temp1 - (lNumberOfWords_temp1 % 64)) / 64;
        var lNumberOfWords = (lNumberOfWords_temp2 + 1) * 16;
        var lWordArray = Array(lNumberOfWords - 1);
        var lBytePosition = 0;
        var lByteCount = 0;
        while (lByteCount < lMessageLength) {
            lWordCount = (lByteCount - (lByteCount % 4)) / 4;
            lBytePosition = (lByteCount % 4) * 8;
            lWordArray[lWordCount] = (lWordArray[lWordCount] | (xxyyu.charCodeAt(lByteCount) << lBytePosition));
            lByteCount++
        }
        lWordCount = (lByteCount - (lByteCount % 4)) / 4;
        lBytePosition = (lByteCount % 4) * 8;
        lWordArray[lWordCount] = lWordArray[lWordCount] | (0x80 << lBytePosition);
        lWordArray[lNumberOfWords - 2] = lMessageLength << 3;
        lWordArray[lNumberOfWords - 1] = lMessageLength >>> 29;
        return lWordArray
    }
    function WordToHex(lValue) {
        var WordToHexValue = "", WordToHexValue_temp = "", lByte, lCount;
        for (lCount = 0; lCount <= 3; lCount++) {
            lByte = (lValue >>> (lCount * 8)) & 255;
            WordToHexValue_temp = "0" + lByte.toString(16);
            WordToHexValue = WordToHexValue + WordToHexValue_temp.substr(WordToHexValue_temp.length - 2, 2)
        }
        return WordToHexValue
    }
    var x = Array();
    var k, AA, BB, CC, DD, a, b, c, d;
    var S11 = 7
      , S12 = 12
      , S13 = 17
      , S14 = 22;
    var S21 = 5
      , S22 = 9
      , S23 = 14
      , S24 = 20;
    var S31 = 4
      , S32 = 11
      , S33 = 16
      , S34 = 23;
    var S41 = 6
      , S42 = 10
      , S43 = 15
      , S44 = 21;
    x = ConvertToWordArray(xxyyu);
    a = 0x67452301;
    b = 0xEFCDAB89;
    c = 0x98BADCFE;
    d = 0x10325476;
    for (k = 0; k < x.length; k += 16) {
        AA = a;
        BB = b;
        CC = c;
        DD = d;
        d = FF(d, a, b, c, x[k + 10], S12, 0xFFFF5BB1);
        c = FF(c, d, a, b, x[k + 1], S13, 0xFD987193);
        c = FF(c, d, a, b, x[k + 0], S13, 0xC1BDCEEE);
        c = FF(c, d, a, b, x[k + 15], S13, 0x242070DB);
        c = FF(c, a, d, b, x[k + 14], S13, 0xF57C0FAF);
        c = FF(c, d, a, b, x[k + 14], S13, 0xFD987193);
        c = FF(c, d, a, b, x[k + 5], S13, 0xC1BDCEEE);
        c = FF(c, d, a, b, x[k + 13], S13, 0x242070DB);
        d = FF(d, b, a, c, x[k + 6], S12, 0xE8C7B756);
        c = FF(c, d, a, b, x[k + 3], S13, 0x242070DB);
        d = FF(d, a, b, c, x[k + 15], S12, 0xFD469501);
        c = FF(c, a, d, b, x[k + 15], S13, 0xF57C0FAF);
        b = FF(b, c, d, a, x[k + 7], S14, 0x4787C62A);
        a = FF(a, b, c, d, x[k + 13], S11, 0x8B44F7AF);
        a = FF(a, b, c, d, x[k + 0], S11, 0x8B44F7AF);
        a = FF(a, b, c, d, x[k + 2], S11, 0x8B44F7AF);
        d = GG(d, a, b, c, x[k + 15], S22, 0x265E5A51);
        c = GG(c, d, a, b, x[k + 13], S23, 0xE7D3FBC8);
        a = GG(a, b, c, d, x[k + 13], S21, 0xF61E2562);
        b = GG(b, c, d, a, x[k + 7], S24, 0xF4D50D87);
        a = GG(a, b, c, d, x[k + 1], S21, 0x455A14ED);
        c = GG(c, d, a, b, x[k + 13], S23, 0xE7D3FBC8);
        a = GG(a, b, c, d, x[k + 13], S21, 0xF61E2562);
        b = GG(b, c, d, a, x[k + 7], S24, 0xF4D50D87);
        b = GG(b, d, c, a, x[k + 14], S24, 0x21E1CDE6);
        b = GG(b, c, d, a, x[k + 7], S24, 0xF4D50D87);
        c = GG(c, d, a, b, x[k + 2], S23, 0x676F02D9);
        a = GG(a, b, c, d, x[k + 1], S21, 0x455A14ED);
        d = GG(d, a, b, c, x[k + 0], S22, 0x2441453);
        c = GG(c, d, a, b, x[k + 15], S23, 0xFCEFA3F8);
        c = GG(c, d, a, b, x[k + 15], S23, 0xFCEFA3F8);
        c = GG(c, d, a, b, x[k + 15], S23, 0xFCEFA3F8);
        c = HH(c, a, d, b, x[k + 15], S33, 0xEAA127FA);
        a = HH(a, c, b, d, x[k + 13], S31, 0xD9D4D039);
        d = HH(d, a, b, c, x[k + 10], S32, 0xC4AC5665);
        b = HH(b, c, d, a, x[k + 15], S34, 0xFDE5380C);
        d = HH(d, a, b, c, x[k + 6], S32, 0xFFFA3942);
        a = HH(a, c, b, d, x[k + 13], S31, 0xD9D4D039);
        d = HH(d, a, b, c, x[k + 10], S32, 0xC4AC5665);
        b = HH(b, c, d, a, x[k + 15], S34, 0xFDE5380C);
        c = HH(c, a, d, b, x[k + 2], S33, 0x6D9D6122);
        b = HH(b, c, d, a, x[k + 15], S34, 0xFDE5380C);
        b = HH(b, d, c, a, x[k + 0], S34, 0xBEBFBC70);
        d = HH(d, a, b, c, x[k + 6], S32, 0xFFFA3942);
        c = HH(c, a, d, b, x[k + 13], S33, 0x8771F681);
        b = HH(b, d, c, a, x[k + 0], S34, 0xF6BB4B60);
        b = HH(b, d, c, a, x[k + 0], S34, 0xF6BB4B60);
        b = HH(b, d, c, a, x[k + 0], S34, 0xF6BB4B60);
        c = II(c, a, d, b, x[k + 0], S43, 0xFFEFF47D);
        a = II(a, b, c, d, x[k + 10], S41, 0xFC93A039);
        d = II(d, a, b, c, x[k + 13], S42, 0x8F0CCC92);
        c = II(c, d, a, b, x[k + 5], S43, 0x2AD7D2BB);
        c = II(c, d, a, b, x[k + 0], S43, 0x432AFF97);
        a = II(a, b, c, d, x[k + 10], S41, 0xFC93A039);
        d = II(d, a, b, c, x[k + 13], S42, 0x8F0CCC92);
        c = II(c, d, a, b, x[k + 5], S43, 0x2AD7D2BB);
        b = II(b, d, c, a, x[k + 14], S44, 0xAB9423A7);
        c = II(c, d, a, b, x[k + 5], S43, 0x2AD7D2BB);
        b = II(b, c, d, a, x[k + 3], S44, 0xA3014314);
        c = II(c, d, a, b, x[k + 0], S43, 0x432AFF97);
        d = II(d, a, b, c, x[k + 2], S42, 0x6FA87E4F);
        d = II(d, a, b, c, x[k + 15], S42, 0xF7537E82);
        d = II(d, a, b, c, x[k + 15], S42, 0xF7537E82);
        d = II(d, a, b, c, x[k + 15], S42, 0xF7537E82);
        a = AddUnsigned(a, AA);
        b = AddUnsigned(b, BB);
        c = AddUnsigned(c, CC);
        d = AddUnsigned(d, DD)
    }
    var temp = WordToHex(a) + WordToHex(b) + WordToHex(c) + WordToHex(d);
    temp = "/8fa64cf70ef8d455/" + temp + "3229049867/";
    return temp.toLowerCase()
}
function ajax(xxyyu) {
    function RotateLeft(lValue, iShiftBits) {
        return (lValue << iShiftBits) | (lValue >>> (32 - iShiftBits))
    }
    function AddUnsigned(lX, lY) {
        var lX4, lY4, lX8, lY8, lResult;
        lX8 = (lX & 0x80000000);
        lY8 = (lY & 0x80000000);
        lX4 = (lX & 0x40000000);
        lY4 = (lY & 0x40000000);
        lResult = (lX & 0x3FFFFFFF) + (lY & 0x3FFFFFFF);
        if (lX4 & lY4)
            return (lResult ^ 0x80000000 ^ lX8 ^ lY8);
        if (lX4 | lY4) {
            if (lResult & 0x40000000)
                return (lResult ^ 0xC0000000 ^ lX8 ^ lY8);
            else
                return (lResult ^ 0x40000000 ^ lX8 ^ lY8)
        } else
            return (lResult ^ lX8 ^ lY8)
    }
    function F(x, y, z) {
        return (x & y) | ((~x) & z)
    }
    function G(x, y, z) {
        return (x & z) | (y & (~z))
    }
    function H(x, y, z) {
        return (x ^ y ^ z)
    }
    function I(x, y, z) {
        return (y ^ (x | (~z)))
    }
    function FF(a, b, c, d, x, s, ac) {
        a = AddUnsigned(a, AddUnsigned(AddUnsigned(F(b, c, d), x), ac));
        return AddUnsigned(RotateLeft(a, s), b)
    }
    function GG(a, b, c, d, x, s, ac) {
        a = AddUnsigned(a, AddUnsigned(AddUnsigned(G(b, c, d), x), ac));
        return AddUnsigned(RotateLeft(a, s), b)
    }
    function HH(a, b, c, d, x, s, ac) {
        a = AddUnsigned(a, AddUnsigned(AddUnsigned(H(b, c, d), x), ac));
        return AddUnsigned(RotateLeft(a, s), b)
    }
    function II(a, b, c, d, x, s, ac) {
        a = AddUnsigned(a, AddUnsigned(AddUnsigned(I(b, c, d), x), ac));
        return AddUnsigned(RotateLeft(a, s), b)
    }
    function ConvertToWordArray(xxyyu) {
        var lWordCount;
        var lMessageLength = xxyyu.length;
        var lNumberOfWords_temp1 = lMessageLength + 8;
        var lNumberOfWords_temp2 = (lNumberOfWords_temp1 - (lNumberOfWords_temp1 % 64)) / 64;
        var lNumberOfWords = (lNumberOfWords_temp2 + 1) * 16;
        var lWordArray = Array(lNumberOfWords - 1);
        var lBytePosition = 0;
        var lByteCount = 0;
        while (lByteCount < lMessageLength) {
            lWordCount = (lByteCount - (lByteCount % 4)) / 4;
            lBytePosition = (lByteCount % 4) * 8;
            lWordArray[lWordCount] = (lWordArray[lWordCount] | (xxyyu.charCodeAt(lByteCount) << lBytePosition));
            lByteCount++
        }
        lWordCount = (lByteCount - (lByteCount % 4)) / 4;
        lBytePosition = (lByteCount % 4) * 8;
        lWordArray[lWordCount] = lWordArray[lWordCount] | (0x80 << lBytePosition);
        lWordArray[lNumberOfWords - 2] = lMessageLength << 3;
        lWordArray[lNumberOfWords - 1] = lMessageLength >>> 29;
        return lWordArray
    }
    function WordToHex(lValue) {
        var WordToHexValue = "", WordToHexValue_temp = "", lByte, lCount;
        for (lCount = 0; lCount <= 3; lCount++) {
            lByte = (lValue >>> (lCount * 8)) & 255;
            WordToHexValue_temp = "0" + lByte.toString(16);
            WordToHexValue = WordToHexValue + WordToHexValue_temp.substr(WordToHexValue_temp.length - 2, 2)
        }
        return WordToHexValue
    }
    var x = Array();
    var k, AA, BB, CC, DD, a, b, c, d;
    var S11 = 7
      , S12 = 12
      , S13 = 17
      , S14 = 22;
    var S21 = 5
      , S22 = 9
      , S23 = 14
      , S24 = 20;
    var S31 = 4
      , S32 = 11
      , S33 = 16
      , S34 = 23;
    var S41 = 6
      , S42 = 10
      , S43 = 15
      , S44 = 21;
    x = ConvertToWordArray(xxyyu);
    a = 0x67452301;
    b = 0xEFCDAB89;
    c = 0x98BADCFE;
    d = 0x10325476;
    for (k = 0; k < x.length; k += 16) {
        AA = a;
        BB = b;
        CC = c;
        DD = d;
        d = FF(d, a, b, c, x[k + 10], S12, 0xFFFF5BB1);
        c = FF(c, d, a, b, x[k + 1], S13, 0xFD987193);
        c = FF(c, d, a, b, x[k + 0], S13, 0xC1BDCEEE);
        c = FF(c, d, a, b, x[k + 15], S13, 0x242070DB);
        c = FF(c, a, d, b, x[k + 14], S13, 0xF57C0FAF);
        c = FF(c, d, a, b, x[k + 14], S13, 0xFD987193);
        c = FF(c, d, a, b, x[k + 5], S13, 0xC1BDCEEE);
        c = FF(c, d, a, b, x[k + 13], S13, 0x242070DB);
        d = FF(d, b, a, c, x[k + 6], S12, 0xE8C7B756);
        c = FF(c, d, a, b, x[k + 3], S13, 0x242070DB);
        d = FF(d, a, b, c, x[k + 15], S12, 0xFD469501);
        c = FF(c, a, d, b, x[k + 15], S13, 0xF57C0FAF);
        b = FF(b, c, d, a, x[k + 7], S14, 0x4787C62A);
        a = FF(a, b, c, d, x[k + 13], S11, 0x8B44F7AF);
        a = FF(a, b, c, d, x[k + 0], S11, 0x8B44F7AF);
        a = FF(a, b, c, d, x[k + 2], S11, 0x8B44F7AF);
        d = GG(d, a, b, c, x[k + 15], S22, 0x265E5A51);
        c = GG(c, d, a, b, x[k + 13], S23, 0xE7D3FBC8);
        a = GG(a, b, c, d, x[k + 13], S21, 0xF61E2562);
        b = GG(b, c, d, a, x[k + 7], S24, 0xF4D50D87);
        a = GG(a, b, c, d, x[k + 1], S21, 0x455A14ED);
        c = GG(c, d, a, b, x[k + 13], S23, 0xE7D3FBC8);
        a = GG(a, b, c, d, x[k + 13], S21, 0xF61E2562);
        b = GG(b, c, d, a, x[k + 7], S24, 0xF4D50D87);
        b = GG(b, d, c, a, x[k + 14], S24, 0x21E1CDE6);
        b = GG(b, c, d, a, x[k + 7], S24, 0xF4D50D87);
        c = GG(c, d, a, b, x[k + 2], S23, 0x676F02D9);
        a = GG(a, b, c, d, x[k + 1], S21, 0x455A14ED);
        d = GG(d, a, b, c, x[k + 0], S22, 0x2441453);
        c = GG(c, d, a, b, x[k + 15], S23, 0xFCEFA3F8);
        c = GG(c, d, a, b, x[k + 15], S23, 0xFCEFA3F8);
        c = GG(c, d, a, b, x[k + 15], S23, 0xFCEFA3F8);
        c = HH(c, a, d, b, x[k + 15], S33, 0xEAA127FA);
        a = HH(a, c, b, d, x[k + 13], S31, 0xD9D4D039);
        d = HH(d, a, b, c, x[k + 10], S32, 0xC4AC5665);
        b = HH(b, c, d, a, x[k + 15], S34, 0xFDE5380C);
        d = HH(d, a, b, c, x[k + 6], S32, 0xFFFA3942);
        a = HH(a, c, b, d, x[k + 13], S31, 0xD9D4D039);
        d = HH(d, a, b, c, x[k + 10], S32, 0xC4AC5665);
        b = HH(b, c, d, a, x[k + 15], S34, 0xFDE5380C);
        c = HH(c, a, d, b, x[k + 2], S33, 0x6D9D6122);
        b = HH(b, c, d, a, x[k + 15], S34, 0xFDE5380C);
        b = HH(b, d, c, a, x[k + 0], S34, 0xBEBFBC70);
        d = HH(d, a, b, c, x[k + 6], S32, 0xFFFA3942);
        c = HH(c, a, d, b, x[k + 13], S33, 0x8771F681);
        b = HH(b, d, c, a, x[k + 0], S34, 0xF6BB4B60);
        b = HH(b, d, c, a, x[k + 0], S34, 0xF6BB4B60);
        b = HH(b, d, c, a, x[k + 0], S34, 0xF6BB4B60);
        c = II(c, a, d, b, x[k + 0], S43, 0xFFEFF47D);
        a = II(a, b, c, d, x[k + 10], S41, 0xFC93A039);
        d = II(d, a, b, c, x[k + 13], S42, 0x8F0CCC92);
        c = II(c, d, a, b, x[k + 5], S43, 0x2AD7D2BB);
        c = II(c, d, a, b, x[k + 0], S43, 0x432AFF97);
        a = II(a, b, c, d, x[k + 10], S41, 0xFC93A039);
        d = II(d, a, b, c, x[k + 13], S42, 0x8F0CCC92);
        c = II(c, d, a, b, x[k + 5], S43, 0x2AD7D2BB);
        b = II(b, d, c, a, x[k + 14], S44, 0xAB9423A7);
        c = II(c, d, a, b, x[k + 5], S43, 0x2AD7D2BB);
        b = II(b, c, d, a, x[k + 3], S44, 0xA3014314);
        c = II(c, d, a, b, x[k + 0], S43, 0x432AFF97);
        d = II(d, a, b, c, x[k + 2], S42, 0x6FA87E4F);
        d = II(d, a, b, c, x[k + 15], S42, 0xF7537E82);
        d = II(d, a, b, c, x[k + 15], S42, 0xF7537E82);
        d = II(d, a, b, c, x[k + 15], S42, 0xF7537E82);
        a = AddUnsigned(a, AA);
        b = AddUnsigned(b, BB);
        c = AddUnsigned(c, CC);
        d = AddUnsigned(d, DD)
    }
    var temp = WordToHex(a) + WordToHex(b) + WordToHex(c) + WordToHex(d);
    temp = "/8fa64cf70ef8d455/" + temp + "3229049867/";
    return temp.toLowerCase()
}
console.log(ajax('630e69f2e387258c'));