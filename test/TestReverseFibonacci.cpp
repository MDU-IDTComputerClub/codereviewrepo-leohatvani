/*
Unit tests for ReverseFibonacci class
*/

#include "../ReverseFibonacci.h"
#include <gtest/gtest.h>

TEST(ReverseFibonacci, Print)
{
  ReverseFibonacci rf(6);
  testing::internal::CaptureStdout();
  rf.print();
  std::string output = testing::internal::GetCapturedStdout();
  EXPECT_EQ("8 5 3 2 1 1 \n", output);
}

TEST(ReverseFibonacci, Destructor)
{
  testing::internal::CaptureStdout();
  {
    ReverseFibonacci rf(5);
  }
  std::string output = testing::internal::GetCapturedStdout();
  EXPECT_EQ("Object destroyed\n", output);
}
