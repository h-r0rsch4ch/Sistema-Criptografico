// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract TextStorage {
    string private storedText;

    function sendData(string memory data) public {
        storedText = data;
    }

    function getData() public view returns (string memory) {
        return storedText;
    }
}
