#!/usr/bin/env python

import argparse

def parserArgs():
    parser = argparse.ArgumentParser(description="The parent parser")
    subparsers = parser.add_subparsers()

    parser_create = subparsers.add_parser('create')
    parser_create.add_argument('-z', type=int, default=1)
    parser_create.add_argument('-p', type=int)
    parser_create.set_defaults(func=create)

    parser_update = subparsers.add_parser("update")
    parser_update.add_argument('-p',type=int)

    args = parser.parse_args()
    return args

def create(args):
    if args.z is not None:
        print '((z = %s))' % args.z
    if args.p is not None:
        print '((p = %s))' % args.p

args = parserArgs()

args.func(args)

#if args.P == 1:
#    print ("test")

