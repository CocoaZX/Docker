//
//  ViewController.m
//  methodswizzling
//
//  Created by 张鑫 on 2018/11/30.
//  Copyright © 2018 com.6art.www. All rights reserved.
//

#import "ViewController.h"
#import <objc/runtime.h>

@interface ViewController ()

@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    [self testMethod];
    // Do any additional setup after loading the view, typically from a nib.
}

- (void)testMethod{
    
}

+ (void)load {
    static dispatch_once_t onceToken;
    dispatch_once(&onceToken, ^{
        Class class = [self class];
        
        SEL originalSelector = @selector(viewWillAppear:);
        SEL swizzledSelector = @selector(mrc_viewWillAppear:);
        
        Method originalMethod = class_getInstanceMethod(class, originalSelector);
        Method swizzledMethod = class_getInstanceMethod(class, swizzledSelector);
        
        BOOL success = class_addMethod(class, originalSelector, method_getImplementation(swizzledMethod), method_getTypeEncoding(swizzledMethod));
        if (success) {
            //被替换的方法是父类实现的，class_addMethod添加成功.class_getInstanceMethod返回的Method就是父类的实现。需要替换父类的方法
            class_replaceMethod(class, swizzledSelector, method_getImplementation(originalMethod), method_getTypeEncoding(originalMethod));
        } else {
            //被替换的方法如果本类实现了，class_addMethod就不会成功.class_getInstanceMethod返回的Method就是本类的实现。直接替换
            method_exchangeImplementations(originalMethod, swizzledMethod);
        }
    });
}

+ (void)testMethod{
    
}

#pragma mark - Method Swizzling

//-(void)viewWillAppear:(BOOL)animated{
//    
//}

- (void)mrc_viewWillAppear:(BOOL)animated {
    [self mrc_viewWillAppear:animated];
//    [MobClick beginLogPageView:NSStringFromClass([self class])];
}

@end
