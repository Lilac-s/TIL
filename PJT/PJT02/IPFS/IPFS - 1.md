# IPFS - 1

목표 : 스마트 컨트랙트 구현, 테스트 코드를 통해 구현 완료하기



## NFT 토큰 표준 이해

- Non-Fungible Token Standard
  - [ERC-721 표준 공식 문서](https://eips.ethereum.org/EIPS/eip-721)

- Standard Inferface Detection
  - 필수로 구현해야 하는 함수가 구현되었는지 검증하는 표준
  - [ERC-165](https://eips.ethereum.org/EIPS/eip-165)

- NFT 필수 구현 함수 목록

|                   | 설명                                                         |
| ----------------- | ------------------------------------------------------------ |
| balanceOf         | 특정 사용자 보유하고 있는 NFT 수 반환                        |
| ownerOf           | 특정 NFT의 소유자 주소를 반환                                |
| tokenURI          | 특정 NFT의 원본 데이터가 어디에 저장되어 있는지 URI 반환     |
| approve           | 특정 주소에게 호출 주소가 보유한 NFT의 전송 권한을 부여함.   |
| getApproved       | 특정 NFT의 전송 권한을 부여받은(approved) 주소를 반환        |
| setApprovalForAll | NFT 소유자가 해당 주소에게 모든 NFT의 전송 권한을 부여함.    |
| isApprovalForAll  | 특정 주소에게 모든 전송 권한이 있는지 판별함.                |
| transferFrom      | NFT 전송                                                     |
| safeTransferFrom  | NFT 전송 시 받을 주소가 CA(Contract Address, 스마트 컨트랙트의 주소를 일컬음)가 아닌 EOA(Externally Owned Address)인지 확인하고 EOA면 전송함. |

[OpenZeppelin](https://www.openzeppelin.com/) - 소스코드 참고


